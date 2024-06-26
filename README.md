# 🐲 dragonion

Most **modern-looking**, **encrypted** and functional **in-console** onion chat
that **you** control!!
---

## 📜 Table of Contents

* [🐲 dragonion](#-dragonion)
  * [📜 Table of Contents](#-table-of-contents)
  * [📝 Note](#-note)
  * [🛣️ Usage plan](#-usage-plan)
  * [💻 Usage guide](#-usage-guide)
  * [🔧 Configuration guide](#-configuration-guide)
  * [📃 Credits](#-credits)

---

## 📝 Note

dragonion IS NOT a chat for everyday use. It is **specific** application focused on
**privacy** and **safety**. It can contain functions, that you won't like or don't
contain some functions you would like to have in regular chat application.
You need to set up [[dragonion-server](https://github.com/kotikotprojects/dragonion-server)]
by yourself or using existing server, hosted by your guild/organisation.
We don't provide any official servers.

---

## 🛣️ Usage plan

1. Check [[📜 Table of Contents](#-table-of-contents)] (optionally)
2. Read [[📝 Note](#-note)]
3. Read [[🛣️ Usage guide](#-usage-guide)]
4. Go to [[⚙️ Configuration guide](#-configuration-guide)], choose your
   platform, navigate to opted installation method (they are arranged from most to least
   recommended)
5. Make sure you have access to an up-to-date service provided by an administrator or
   friends, or run your own personal service using the
   [[dragonion-server](https://github.com/kotikotprojects/dragonion-server)]
6. Install pre-requirements, install app, run it,
   checking [[💻 Usage guide](#-usage-guide)] if needed

---

## 💻 Usage guide

To use dragonion-server, you need to install it first. To do this, you can visit
[[Configuration guide](#-configuration-guide)].

If you have questions that are not described in the documentation, you can chat with
[[AI based on this repository](https://chat.collectivai.com/kotikotprojects/dragonion)]

dragonion is **textual** application. It means, that it works **entirely** in the
terminal, while having a **modern design** and user experience that does not differ
from ordinary applications.

When using the application, you will come across terms such as **services**
and **rooms**.

- **Services** from the user's point of view is **a pair of id-key** or **.auth file**
  that you received from the administrator of your organization/guild or your friends.
- The so-called **rooms** are sections of the service that **separate users** and
  make their communication **private** by protecting the rooms with a **password**.
  Rooms **do not have** a "correct" or "incorrect" password. Rooms with the **same**
  name and password - **the same room**, rooms with the same name but **different**
  password - **different** rooms (similarly with other situations, to get into
  **one room** with the interlocutors - **everyone** must enter the **same**
  name-password combination)

Let's say that you have a friend who suggested you connect via encrypted dragonion chat.
In this case, friend most likely provided you with either two strings
(service id and auth string) or an .auth file. Below, we will figure out what to do in
each of these situations.

If not, you will most likely have to start the server yourself.
It doesn't require any special programming or computer skills, but it can be a little
more difficult than starting a chat.
Check [[dragonion-server](https://github.com/kotikotprojects/dragonion-server)] page to get
more information about starting your own dragonion service.

After you have received the options for authentication, you need to install dragonion.
To do this, you can use the [[🔧 Configuration guide](#-configuration-guide)] or ask
a question to [[AI](https://chat.collectivai.com/kotikotprojects/dragonion)],
specifying your platform and choosing the appropriate installation method for yourself.

With the program installed, you can proceed to launch and authenticate. If you have
an .auth file, you need to copy it to the working directory of the program or run
dragonion from the directory that contains this file. If there are authentication
strings, you just need to save them for yourself and paste them into the appropriate
fields at startup.

Start app using `dragonion` command or running executable, you will see user-friendly
interface. Remember, that if you do not understand any part of the interface,
you can always ask [[AI](https://chat.collectivai.com/kotikotprojects/dragonion)] for help.

dragonion also has cli options to automate startup.

- `--auth` or `-a` specifies service name. If `service_name.auth` file exists in working
  directory, first screen with entering auth data will be skipped.
- `--username` or `-u` used to specify username to skip second screen of launch.
- `--connect` or `-c` to start connecting right after application launch and entering
  user and auth information.
- `--dev-proxy-port` is used for development and specifies local proxy port through
  which the dragonion will connect to the torus to skip the step of starting the
  internal proxy.

Use `/connect` and `/join room password` commands to manage connection. Also, you
can get in-application help using `/help` command in chat input. If something is
unclear, use [[AI](https://chat.collectivai.com/kotikotprojects/dragonion)] to figure out
what to do in this situation.

---

## 🔧 Configuration guide

You can use [[pipx](https://pypa.github.io/pipx/)] to install dragonion:
```commandline
pipx install dragonion
```
Or download pre-built executable:
- [🪟 Windows](https://github.com/kotikotprojects/dragonion/releases/latest/download/dragonion-win32.exe)
- [🐧 Linux](https://github.com/kotikotprojects/dragonion/releases/latest/download/dragonion-linux)
- [🍎 MacOS](https://github.com/kotikotprojects/dragonion/releases/latest/download/dragonion-darwin)

If you are missing something, you use non-x64 (ARM) or Android system or just want to 
have more installation options, consider checking sections below.

### Windows
<details> <summary>
Windows guide
</summary>
There are several different ways to install the program available, they are arranged
from the most convenient and easily updated, to the less obvious, but perhaps more
convenient for you:

<details> <summary>Single standalone executable</summary>

#### Single standalone executable
This method provides the ability to download a single executable file that leaves no
traces and is convenient for copying or using.

#### Pre-requirements
- [[Windows terminal](https://github.com/microsoft/terminal)] is recommended,
  [[install it from Microsoft Store](https://aka.ms/terminal)]

#### Fresh installation
- [[Download latest version](https://github.com/kotikotprojects/dragonion/releases/latest/download/dragonion-win32.exe)]
- Copy file in any folder and locate `.auth` files in that folder

#### Launch options
- Run from commandline (Windows Terminal recommended) or by double-clicking executable.
  If double-clicking, `.auth` files need to be located near executable, if running from
  commandline, they need to be located in workdir.

#### Updating
- Re-download latest version from link above and replace the file.

[[Back to Usage guide](#-usage-guide)]

</details>

<details> <summary>Installation script</summary>

#### Installation script
This method provides a way to install non-portable, but standalone application, using
one installation script

#### Pre-requirements
- [[Windows terminal](https://github.com/microsoft/terminal)] is recommended,
  [[install it from Microsoft Store](https://aka.ms/terminal)]

#### Fresh installation
- Using powershell, navigate to folder where you want to be dragonion installed. In 
folder where you will run script, `dragonion` folder will be created.
- Run:
```powershell
iwr https://s.kotikot.com/dragonion/w | iex
```
- After running this command, press Enter and wait.

#### Launch options
- After installation finishes, script will output full installation path (with 
executable name). You can paste it in terminal to run dragonion.
- Other option is to copy `dragonion.exe` from `dragonion\Scripts` somewhere and 
launch it. But remember, that you cannot move installation folder, app isn't portable.

#### Updating
- Navigate to folder, where `dragonion` installation folder is located.
- Run:
```powershell
iwr https://s.kotikot.com/dragonion/wu | iex
```

#### Script mirrors:
Installation:
```powershell
iwr https://s.kotikot.com/dragonion/w | iex
iwr https://github.com/kotikotprojects/dragonion/raw/master/scripts/w | iex
iwr https://pastebin.com/raw/ix3LtZqj | iex
```

Updating:
```powershell
iwr https://s.kotikot.com/dragonion/wu | iex
iwr https://github.com/kotikotprojects/dragonion/raw/master/scripts/wu | iex
iwr https://pastebin.com/raw/Z28JDDMi | iex
```

[[Back to Usage guide](#-usage-guide)]

</details>

<details> <summary>Using pipx</summary>

#### Using pipx
This method provides a way to install dragonion via pipx. It is very fast way of 
installation and very convenient for using, but has some pre-requirements to install
on target system.

#### Pre-requirements
- [[Python3](https://www.python.org/downloads/)] (with pip)
- [[pipx](https://pypa.github.io/pipx)], relaunch shell after installation

```powershell
pip install pipx --user
python -m pipx ensurepath
```
- [[Windows terminal](https://github.com/microsoft/terminal)] is recommended,
  [[install it from Microsoft Store](https://aka.ms/terminal)]

#### Fresh installation
```powershell
pipx install dragonion
```

#### Launch options
- Run `dragonion` in terminal

#### Updating
```powershell
pipx upgrade dragonion
```

[[Back to Usage guide](#-usage-guide)]

</details>

<details> <summary>Python venv and pip</summary>

#### Python venv and pip
This method provides a way of installation using python in virtual environment and 
installing application from repo.

#### Pre-requirements
- [[Python3](https://www.python.org/downloads/)] (with pip)
- [[Git](https://git-scm.com/download/win)]
- [[Windows terminal](https://github.com/microsoft/terminal)] is recommended,
  [[install it from Microsoft Store](https://aka.ms/terminal)]

#### Fresh installation
```commandline
git clone https://github.com/kotikotprojects/dragonion
cd dragonion
python -m venv venv
venv\Scripts\activate
pip install .
```

#### Launch options
- After fresh install, run `dragonion` in environment 
(or `python -m dragonion`)
- `cd` to app folder, run `venv\Scripts\activate`, than `dragonion` in 
environment (`python -m dragonion`)
- Run `dragonion.exe` from `venv\Scripts`. You can also copy it anywhere you
want, but remember that data and config files are saved near executable file

#### Updating
`cd` to app directory, than 
```commandline
git pull
```
If there are new changes, run
```commandline
venv\Scripts\activate
pip install .
```

[[Back to Usage guide](#-usage-guide)]

</details>

<details> <summary>Building from .whl</summary>

#### Building from .whl
This method provides a way of installation using python in virtual environment and 
installing application from repo.

#### Pre-requirements
- [[Python3](https://www.python.org/downloads/)] (with pip)
- [[Windows terminal](https://github.com/microsoft/terminal)] is recommended,
  [[install it from Microsoft Store](https://aka.ms/terminal)]

#### Fresh installation
- Download [[latest wheel](https://github.com/kotikotprojects/dragonion/releases/latest/download/dragonion-universal-py3-none-any.whl)]
```commandline
python -m venv dragonion
dragonion\Scripts\activate
pip install dragonion-universal-py3-none-any.whl
```

#### Launch options
- After fresh install, run `dragonion` in environment 
(or `python -m dragonion`)
- `cd` to app folder, run `dragonion\Scripts\activate`, than `dragonion` in 
environment (`python -m dragonion`)
- Run `dragonion.exe` from `dragonion\Scripts`. You can also copy it anywhere you
want, but remember that data and config files are saved near executable file

#### Updating
- Download [[latest wheel](https://github.com/kotikotprojects/dragonion/releases/latest/download/dragonion-universal-py3-none-any.whl)]
```commandline
dragonion\Scripts\activate
pip install dragonion-universal-py3-none-any.whl
```

[[Back to Usage guide](#-usage-guide)]

</details>
</details>

### Linux
<details><summary>
Linux guide
</summary>
Installation methods depend on your processor architecture. Choose the one that suits 
you. In sections, different ways to install the program are arranged
from the most convenient and easily updated, to the less obvious, but perhaps more
convenient for you:

<details><summary>x64</summary> 

<details> <summary>Using pipx</summary>

#### Using pipx
This method provides a way to install dragonion via pipx. It is very fast way of 
installation and very convenient for using.

#### Pre-requirements
- `python3`, `python3-pip`, `python3-venv`

#### Fresh installation
- Install pipx and relaunch shell
```commandline
pip install pipx --user
python3 -m pipx ensurepath
```
- Install dragonion
```commandline
pipx install dragonion
```

#### Launch options
- Run `dragonion` in terminal

#### Updating
```powershell
pipx upgrade dragonion
```

[[Back to Usage guide](#-usage-guide)]

</details>

<details> <summary>Single standalone executable</summary>

#### Single standalone executable
This method provides the ability to download a single executable file that leaves no 
traces and is convenient for copying or using.

#### Pre-requirements
- No special requirements found on regular distros

#### Fresh installation
- [[Download latest version](https://github.com/kotikotprojects/dragonion/releases/latest/download/dragonion-linux)]
- Copy file in any folder and locate `.auth` files in that folder

#### Launch options
- Run from commandline `dragonion-linux`, `.auth` files should be located in workdir

#### Updating
Re-download latest version from link above and replace the file.

[[Back to Usage guide](#-usage-guide)]

</details>

<details> <summary>Installation script</summary>

#### Installation script
This method provides a way to install non-portable, but standalone application, using
one installation script.

#### Pre-requirements
- `python3` `python3-pip` `python3-venv` `wget`

#### Fresh installation
- Using your shell, navigate to directory where you want to be dragonion installed. In 
folder where you will run script, `dragonion` dir will be created.
- Run:
```bash
. <(wget -qO- https://s.kotikot.com/dragonion/l)
```
- After running this command, press Enter and wait.
#### Launch options
- After installation finishes, script will output full installation path (with 
executable name). You can paste it in terminal to run dragonion.
- Also, after installation you will be in dragonion environment, so you can run
`dragonion` as command. To deactivate it, you can run `deactivate`, and to activate
again, use `. dragonion/bin/activate`
- Other option is to copy `dragonion` from `dragonion\bin` somewhere and 
launch it. But remember, that you cannot move installation dir, app isn't portable.

#### Updating
- Navigate to directory, where `dragonion` installation dir is located.
- Run:
```bash
. <(wget -qO- https://s.kotikot.com/dragonion/lu)
```

#### Script mirrors:
Installation:
```bash
. <(wget -qO- https://s.kotikot.com/dragonion/l)
. <(wget -qO- https://github.com/kotikotprojects/dragonion/raw/master/scripts/l)
. <(wget -qO- https://pastebin.com/raw/LdrRBEYB)
```

Updating:
```bash
. <(wget -qO- https://s.kotikot.com/dragonion/lu)
. <(wget -qO- https://github.com/kotikotprojects/dragonion/raw/master/scripts/lu)
. <(wget -qO- https://pastebin.com/raw/XRSA9wUz)
```

[[Back to Usage guide](#-usage-guide)]

</details>

<details> <summary>Python venv and pip</summary>

#### Python venv and pip
This method provides a way of installation using python in virtual environment and 
installing application from repo.

#### Pre-requirements
- `python3` `python3-pip` `python3-venv`
- `git`


#### Fresh installation
```commandline
git clone https://github.com/kotikotprojects/dragonion
cd dragonion
python3 -m venv venv
. venv\bin\activate
pip install .
```

#### Launch options
- After fresh install, run `dragonion` in environment 
(or `python3 -m dragonion`)
- `cd` to app folder, run `. venv\bin\activate`, than `dragonion` in 
environment (`python3 -m dragonion`)
- Run `dragonion` from `venv\bin`. You can also copy it anywhere you
want, but remember that data and config files are saved near executable file

#### Updating
`cd` to app directory, than 
```
git pull
```
If there are new changes, run
```
. venv\bin\activate
pip install .
```

[[Back to Usage guide](#-usage-guide)]

</details>

<details> <summary>Building from .whl</summary>

#### Building from .whl
This method provides a way of installation using python in virtual environment and 
installing application from repo.

#### Pre-requirements
- `python3` `python3-pip` `python3-venv`

#### Fresh installation
- Download [[latest wheel](https://github.com/kotikotprojects/dragonion/releases/latest/download/dragonion-universal-py3-none-any.whl)]
```
python3 -m venv dragonion
. dragonion\bin\activate
pip install dragonion-universal-py3-none-any.whl
```

#### Launch options
- After fresh install, run `dragonion` in environment 
(or `python3 -m dragonion`)
- `cd` to app folder, run `. dragonion\bin\activate`, than `dragonion` in 
environment (`python3 -m dragonion`)
- Run `dragonion` from `dragonion\bin`. You can also copy it anywhere you
want, but remember that data and config files are saved near executable file

#### Updating
- Download [[latest wheel](https://github.com/kotikotprojects/dragonion/releases/latest/download/dragonion-universal-py3-none-any.whl)]
```
. dragonion\bin\activate
pip install dragonion-universal-py3-none-any.whl
```

[[Back to Usage guide](#-usage-guide)]

</details>

</details>

<details><summary>arm</summary>

#### ARM

Tor does not provide expert bundles for arm systems (except macOS). 
You need to install `tor` through your package manager, which is indicated in the 
pre-requirements

<details> <summary>Using pipx</summary>

#### Using pipx
This method provides a way to install dragonion via pipx. It is very fast way of 
installation and very convenient for using.

#### Pre-requirements
- `python3`, `python3-pip`, `python3-venv`
- `tor`

#### Fresh installation
- Install pipx and relaunch shell
```commandline
pip install pipx --user
python3 -m pipx ensurepath
```
- Install dragonion
```commandline
pipx install dragonion
```

#### Launch options
- Run `dragonion` in terminal

#### Updating
```powershell
pipx upgrade dragonion
```

[[Back to Usage guide](#-usage-guide)]

</details>

<details> <summary>Installation script</summary>

#### Installation script
This method provides a way to install non-portable, but standalone application, using
one installation script.

#### Pre-requirements
- `python3` `python3-pip` `python3-venv` `wget`
- `tor`

#### Fresh installation
- Using your shell, navigate to directory where you want to be dragonion installed. In 
folder where you will run script, `dragonion` dir will be created.
- Run:
```bash
. <(wget -qO- https://s.kotikot.com/dragonion/l)
```
- After running this command, press Enter and wait.
#### Launch options
- After installation finishes, script will output full installation path (with 
executable name). You can paste it in terminal to run dragonion.
- Also, after installation you will be in dragonion environment, so you can run
`dragonion` as command. To deactivate it, you can run `deactivate`, and to activate
again, use `. dragonion/bin/activate`
- Other option is to copy `dragonion` from `dragonion\bin` somewhere and 
launch it. But remember, that you cannot move installation dir, app isn't portable.

#### Updating
- Navigate to directory, where `dragonion` installation dir is located.
- Run:
```bash
. <(wget -qO- https://s.kotikot.com/dragonion/lu)
```

#### Script mirrors:
Installation:
```bash
. <(wget -qO- https://s.kotikot.com/dragonion/l)
. <(wget -qO- https://github.com/kotikotprojects/dragonion/raw/master/scripts/l)
. <(wget -qO- https://pastebin.com/raw/LdrRBEYB)
```

Updating:
```bash
. <(wget -qO- https://s.kotikot.com/dragonion/lu)
. <(wget -qO- https://github.com/kotikotprojects/dragonion/raw/master/scripts/lu)
. <(wget -qO- https://pastebin.com/raw/XRSA9wUz)
```

[[Back to Usage guide](#-usage-guide)]

</details>

<details> <summary>Python venv and pip</summary>

#### Python venv and pip
This method provides a way of installation using python in virtual environment and 
installing application from repo.

#### Pre-requirements
- `python3` `python3-pip` `python3-venv`
- `git`
- `tor`


#### Fresh installation
```commandline
git clone https://github.com/kotikotprojects/dragonion
cd dragonion
python3 -m venv venv
. venv\bin\activate
pip install .
```

#### Launch options
- After fresh install, run `dragonion` in environment 
(or `python3 -m dragonion`)
- `cd` to app folder, run `. venv\bin\activate`, than `dragonion` in 
environment (`python3 -m dragonion`)
- Run `dragonion` from `venv\bin`. You can also copy it anywhere you
want, but remember that data and config files are saved near executable file

#### Updating
`cd` to app directory, than 
```
git pull
```
If there are new changes, run
```
. venv\bin\activate
pip install .
```

[[Back to Usage guide](#-usage-guide)]

</details>

<details> <summary>Building from .whl</summary>

#### Building from .whl
This method provides a way of installation using python in virtual environment and 
installing application from repo.

#### Pre-requirements
- `python3` `python3-pip` `python3-venv`
- `tor`

#### Fresh installation
- Download [[latest wheel](https://github.com/kotikotprojects/dragonion/releases/latest/download/dragonion-universal-py3-none-any.whl)]
```
python3 -m venv dragonion
. dragonion\bin\activate
pip install dragonion-universal-py3-none-any.whl
```

#### Launch options
- After fresh install, run `dragonion` in environment 
(or `python3 -m dragonion`)
- `cd` to app folder, run `. dragonion\bin\activate`, than `dragonion` in 
environment (`python3 -m dragonion`)
- Run `dragonion` from `dragonion\bin`. You can also copy it anywhere you
want, but remember that data and config files are saved near executable file

#### Updating
- Download [[latest wheel](https://github.com/kotikotprojects/dragonion/releases/latest/download/dragonion-universal-py3-none-any.whl)]
```
. dragonion\bin\activate
pip install dragonion-universal-py3-none-any.whl
```

[[Back to Usage guide](#-usage-guide)]

</details>

</details>

</details>

### MacOS
<details><summary>
MacOS guide
</summary>

<details> <summary>Using pipx</summary>

#### Using pipx
This method provides a way to install dragonion via pipx. It is very fast way of 
installation and very convenient for using.

#### Pre-requirements
- `python3`, `python3-pip`, `python3-venv`

#### Fresh installation
- Install pipx and relaunch shell
```commandline
brew install pipx
pipx ensurepath
```
- Install dragonion
```commandline
pipx install dragonion
```

#### Launch options
- Run `dragonion` in terminal

#### Updating
```powershell
pipx upgrade dragonion
```

[[Back to Usage guide](#-usage-guide)]

</details>

<details> <summary>Single standalone executable</summary>

#### Single standalone executable
This method provides the ability to download a single executable file that leaves no 
traces and is convenient for copying or using.

#### Pre-requirements
- No special requirements found on regular distros

#### Fresh installation
- [[Download latest version](https://github.com/kotikotprojects/dragonion/releases/latest/download/dragonion-darwin)]
- Copy file in any folder and locate `.auth` files in that folder

#### Launch options
- Run from commandline `dragonion-darwin`, `.auth` files should be located in workdir

#### Updating
Re-download latest version from link above and replace the file.

[[Back to Usage guide](#-usage-guide)]

</details>

<details> <summary>Installation script</summary>

#### Installation script
This method provides a way to install non-portable, but standalone application, using
one installation script.

#### Pre-requirements
- `python3` `python3-pip` `python3-venv` `wget` `curl`

#### Fresh installation
- Using your shell, navigate to directory where you want to be dragonion installed. In 
folder where you will run script, `dragonion` dir will be created.
- Run:
```bash
bash <(curl -sL https://s.kotikot.com/dragonion/m)
```
- After running this command, press Enter and wait.
#### Launch options
- After installation finishes, script will output full installation path (with 
executable name). You can paste it in terminal to run dragonion.
- Also, after installation you will be in dragonion environment, so you can run
`dragonion` as command. To deactivate it, you can run `deactivate`, and to activate
again, use `. dragonion/bin/activate`
- Other option is to copy `dragonion` from `dragonion\bin` somewhere and 
launch it. But remember, that you cannot move installation dir, app isn't portable.

#### Updating
- Navigate to directory, where `dragonion` installation dir is located.
- Run:
```bash
bash <(curl -sL https://s.kotikot.com/dragonion/lu)
```

#### Script mirrors:
Installation:
```bash
bash <(curl -sL https://s.kotikot.com/dragonion/m)
bash <(curl -sL https://github.com/kotikotprojects/dragonion/raw/master/scripts/m)
bash <(curl -sL https://pastebin.com/raw/4whxpEFD)
```

Updating:
```bash
bash <(curl -sL https://s.kotikot.com/dragonion/mu)
bash <(curl -sL https://github.com/kotikotprojects/dragonion/raw/master/scripts/mu)
bash <(curl -sL https://pastebin.com/raw/DkPhhTyv)
```

[[Back to Usage guide](#-usage-guide)]

</details>

<details> <summary>Python venv and pip</summary>

#### Python venv and pip
This method provides a way of installation using python in virtual environment and 
installing application from repo.

#### Pre-requirements
- `python3` `python3-pip` `python3-venv`
- `git`


#### Fresh installation
```commandline
git clone https://github.com/kotikotprojects/dragonion
cd dragonion
python3 -m venv venv
. venv\bin\activate
pip install .
```

#### Launch options
- After fresh install, run `dragonion` in environment 
(or `python3 -m dragonion`)
- `cd` to app folder, run `. venv\bin\activate`, than `dragonion` in 
environment (`python3 -m dragonion`)
- Run `dragonion` from `venv\bin`. You can also copy it anywhere you
want, but remember that data and config files are saved near executable file

#### Updating
`cd` to app directory, than 
```
git pull
```
If there are new changes, run
```
. venv\bin\activate
pip install .
```

[[Back to Usage guide](#-usage-guide)]

</details>

<details> <summary>Building from .whl</summary>

#### Building from .whl
This method provides a way of installation using python in virtual environment and 
installing application from repo.

#### Pre-requirements
- `python3` `python3-pip` `python3-venv`

#### Fresh installation
- Download [[latest wheel](https://github.com/kotikotprojects/dragonion/releases/latest/download/dragonion-universal-py3-none-any.whl)]
```
python3 -m venv dragonion
. dragonion\bin\activate
pip install dragonion-universal-py3-none-any.whl
```

#### Launch options
- After fresh install, run `dragonion` in environment 
(or `python3 -m dragonion`)
- `cd` to app folder, run `. dragonion\bin\activate`, than `dragonion` in 
environment (`python3 -m dragonion`)
- Run `dragonion` from `dragonion\bin`. You can also copy it anywhere you
want, but remember that data and config files are saved near executable file

#### Updating
- Download [[latest wheel](https://github.com/kotikotprojects/dragonion/releases/latest/download/dragonion-universal-py3-none-any.whl)]
```
. dragonion\bin\activate
pip install dragonion-universal-py3-none-any.whl
```

[[Back to Usage guide](#-usage-guide)]

</details>

</details>

### Android
<details><summary>
Termux guide
</summary>

Due to the nature of Termux, installation can be a little tricky, so we have simplified 
the installation process for you by creating a specific pre-requirements termux guide.

```
pkg install python python-pip libexpat git rust binutils tor
pkg upgrade
```
Now, navigate to [[guide for Linux ARM systems](#arm)] 
([Linux](#linux) -> arm) and choose desired installation
way. They all apply for termux also if pre-requirements above are installed.

</details>

---

## 📃 Credits

- [[OnionShare project](https://github.com/onionshare)] - code inspiration for
  integrating application with tor
