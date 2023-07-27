import os
import traceback
import contextlib
import re


class PrettyException:
    def __init__(self, e: Exception):
        self.pretty_exception = f'❌ Error! Report it to admins: \n' \
                                f'🐊 {e.__traceback__.tb_frame.f_code.co_filename.replace(os.getcwd(), "")}' \
                                f':{e.__traceback__.tb_frame.f_lineno} \n' \
                                f'😍 {e.__class__.__name__} \n' \
                                f'👉 {"".join(traceback.format_exception_only(e)).strip()} \n\n' \
                                f'⬇️ Trace: \n' \
                                f'{self.get_full_stack()}'

    @staticmethod
    def get_full_stack():
        full_stack = traceback.format_exc().replace(
            "Traceback (most recent call last):\n", ""
        )

        line_regex = r'  File "(.*?)", line ([0-9]+), in (.+)'

        def format_line(line: str) -> str:
            filename_, lineno_, name_ = re.search(line_regex, line).groups()
            with contextlib.suppress(Exception):
                filename_ = os.path.basename(filename_)

            return (
                f"🤯 {filename_}:{lineno_} (in {name_} call)"
            )

        full_stack = "\n".join(
            [
                format_line(line)
                if re.search(line_regex, line)
                else f"{line}"
                for line in full_stack.splitlines()
            ]
        )

        return full_stack

    def __str__(self):
        return self.pretty_exception
