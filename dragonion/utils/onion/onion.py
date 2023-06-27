from stem.control import Controller
from stem import SocketClosed

import textwrap
import socket
import random
import os
import psutil
import shlex
import subprocess
import tempfile
import platform
import time

from dragonion.utils.core import dirs


def get_available_port(min_port, max_port):
    with socket.socket() as tmpsock:
        while True:
            try:
                tmpsock.bind(("127.0.0.1", random.randint(min_port, max_port)))
                break
            except OSError:
                pass
        _, port = tmpsock.getsockname()
    return port


class Onion(object):
    c: Controller
    tor_control_socket: str | None
    tor_control_port: int | None
    tor_torrc: str
    tor_socks_port: int
    tor_cookie_auth_file: str
    tor_path: str = dirs.get_tor_paths()
    tor_proc: subprocess.Popen
    connected_to_tor: bool = False
    auth_string: str
    graceful_close_onions: list = list()
    tor_data_directory = tempfile.TemporaryDirectory(
        dir=dirs.build_tmp_dir()
    )
    tor_data_directory_name = tor_data_directory.name
    os.makedirs(os.path.join(tor_data_directory_name, 'auth'))

    def kill_same_tor(self):
        for proc in psutil.process_iter(["pid", "name", "username"]):
            try:
                cmdline = proc.cmdline()
                if (
                        cmdline[0] == self.tor_path
                        and cmdline[1] == "-f"
                        and cmdline[2] == self.tor_torrc
                ):
                    proc.terminate()
                    proc.wait()
                    break
            except Exception as e:
                assert e

    def fill_torrc(self, tor_data_directory_name):
        torrc_template = textwrap.dedent("""
            DataDirectory {data_directory}
            SocksPort {socks_port}
            CookieAuthentication 1
            CookieAuthFile {cookie_auth_file}
            ClientOnionAuthDir {client_onion_auth_dir}
            AvoidDiskWrites 1
            Log notice stdout
        """)
        self.tor_cookie_auth_file = os.path.join(tor_data_directory_name, "cookie")
        try:
            self.tor_socks_port = get_available_port(1000, 65535)
        except Exception as e:
            print(f"Cannot bind any port for socks proxy: {e}")
        self.tor_torrc = os.path.join(tor_data_directory_name, "torrc")

        self.kill_same_tor()

        if platform.system() in ["Windows", "Darwin"]:
            torrc_template += "ControlPort {control_port}\n"
            try:
                self.tor_control_port = get_available_port(1000, 65535)
            except Exception as e:
                print(f"Cannot bind any control port: {e}")
            self.tor_control_socket = None
        else:
            torrc_template += "ControlSocket {control_socket}\n"
            self.tor_control_port = None
            self.tor_control_socket = os.path.join(
                tor_data_directory_name, "control_socket"
            )

        torrc_template = torrc_template.format(
            data_directory=tor_data_directory_name,
            control_port=str(self.tor_control_port),
            control_socket=str(self.tor_control_socket),
            cookie_auth_file=self.tor_cookie_auth_file,
            socks_port=str(self.tor_socks_port),
            client_onion_auth_dir=os.path.join(tor_data_directory_name, 'auth')
        )

        with open(self.tor_torrc, "w") as f:
            f.write(torrc_template)

    def connect(self, connect_timeout=60):
        self.fill_torrc(self.tor_data_directory_name)

        start_ts = time.time()
        if platform.system() == "Windows":
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            self.tor_proc = subprocess.Popen(
                [self.tor_path, "-f", self.tor_torrc],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                startupinfo=startupinfo,
            )
        else:
            env = {"LD_LIBRARY_PATH": os.path.dirname(self.tor_path)}

            self.tor_proc = subprocess.Popen(
                [self.tor_path, "-f", self.tor_torrc],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=env,
            )

        time.sleep(2)

        if platform.system() in ["Windows", "Darwin"]:
            self.c = Controller.from_port(port=self.tor_control_port)
            self.c.authenticate()
        else:
            self.c = Controller.from_socket_file(path=self.tor_control_socket)
            self.c.authenticate()

        while True:
            try:
                res = self.c.get_info("status/bootstrap-phase")
            except SocketClosed:
                raise

            res_parts = shlex.split(res)
            progress = res_parts[2].split("=")[1]
            summary = res_parts[4].split("=")[1]

            print(
                f"\rConnecting to the Tor network: {progress}% - {summary}\033[K",
                end="",
            )

            if summary == "Done":
                print("")
                break
            time.sleep(0.2)

            if time.time() - start_ts > connect_timeout:
                print("")
                try:
                    self.tor_proc.terminate()
                    print(
                        "Taking too long to connect to Tor. Maybe you aren't "
                        "connected to the Internet, or have an inaccurate "
                        "system clock?"
                    )
                    self.cleanup()
                    raise
                except FileNotFoundError:
                    pass

        self.connected_to_tor = True

    def is_authenticated(self):
        if self.c is not None:
            return self.c.is_authenticated()
        else:
            return False

    def cleanup(self):
        if self.tor_proc:
            try:
                rendezvous_circuit_ids = []
                for c in self.c.get_circuits():
                    if (
                            c.purpose == "HS_SERVICE_REND"
                            and c.rend_query in self.graceful_close_onions
                    ):
                        rendezvous_circuit_ids.append(c.id)

                symbols = list("\\|/-")
                symbols_i = 0

                while True:
                    num_rend_circuits = 0
                    for c in self.c.get_circuits():
                        if c.id in rendezvous_circuit_ids:
                            num_rend_circuits += 1

                    if num_rend_circuits == 0:
                        print(
                            "\rTor rendezvous circuits have closed" + " " * 20
                        )
                        break

                    if num_rend_circuits == 1:
                        circuits = "circuit"
                    else:
                        circuits = "circuits"
                    print(
                        f"\rWaiting for {num_rend_circuits} Tor rendezvous {circuits} "
                        f"to close {symbols[symbols_i]} ",
                        end="",
                    )
                    symbols_i = (symbols_i + 1) % len(symbols)
                    time.sleep(1)
            except Exception as e:
                print(e)

            self.tor_proc.terminate()
            time.sleep(0.2)
            if self.tor_proc.poll() is None:
                try:
                    self.tor_proc.kill()
                    time.sleep(0.2)
                except Exception as e:
                    print(e)
            self.tor_proc = None

        self.connected_to_tor = False

        try:
            self.tor_data_directory.cleanup()
        except Exception as e:
            print(f'Cannot cleanup temporary directory: {e}')

    def get_tor_socks_port(self):
        return "127.0.0.1", self.tor_socks_port
