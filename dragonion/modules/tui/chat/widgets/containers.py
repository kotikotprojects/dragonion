from textual.containers import ScrollableContainer
from textual.widget import Widget
from textual.widgets import Static
from textual.containers import Center
from textual import events

import textwrap


class MessagesContainer(ScrollableContainer):
    DEFAULT_CSS = """
    MessagesContainer {
        padding: 1;
        width: 1fr;
        height: 1fr;
        margin-left: 1;
    }
    
    .dragonion_help_logo {
        content-align: center top;
        align-horizontal: center;
        width: 1fr;
        height: auto;
    }
    """

    def _on_mount(self, event: events.Mount) -> None:
        self.mount(
            Static(
                textwrap.dedent("""\
            ██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗██╗ ██████╗ ███╗   ██╗
            ██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██║██╔═══██╗████╗  ██║
            ██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║██║██║   ██║██╔██╗ ██║
            ██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██║██║   ██║██║╚██╗██║
            ██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██║╚██████╔╝██║ ╚████║
            ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                """), classes='dragonion_help_logo'
            ),
            Static(
                "Most modern-looking, encrypted and functional in-console onion "
                "chat that you control! ",
                classes='dragonion_help_logo'
            ),
            Static(
                "Use [bold]/join[/] to connect to room or [bold]/help[/] to get list "
                "of all available commands",
                classes='dragonion_help_logo'
            )
        )

    def scroll_adaptive_to(self, widget: Widget):
        """
        Scrolls to specified widget if user didn't scroll up
        :param widget:
        :return:
        """
        if self.scroll_offset.y == self.max_scroll_y:
            widget.scroll_visible(duration=1)
