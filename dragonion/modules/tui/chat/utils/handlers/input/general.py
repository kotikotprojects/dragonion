from textual.widgets import Input

from .command.command import handle_command
from .message import handle_message


def handle_input_submit():
    from dragonion.modules.tui import app
    field = app.query_one(
        "#chat_input_field",
        expect_type=Input
    )
    message = field.value
    field.value = ""

    if message == '/':
        handle_command(message)
    else:
        handle_message(message)
