from textual.widgets import Static


async def disconnect_command(command_args: list):
    if command_args:
        return 'this command doesn\'t accepts any arguments'

    from dragonion.modules.tui import app

    container = app.query_one('MessagesContainer')

    if onion := app.user_storage.onion:
        onion.cleanup()

    container.mount_scroll(Static("Disconnected from tor \n"))
