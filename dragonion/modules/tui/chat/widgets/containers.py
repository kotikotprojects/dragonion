from textual.containers import ScrollableContainer
from textual.widget import Widget


class MessagesContainer(ScrollableContainer):
    DEFAULT_CSS = """
    Messages {
        padding: 1;
    }
    .chat {
        width: 1fr;
        height: 1fr;
        margin-left: 1;
    }

    .input {
        dock: bottom;
        height: 3;
    }
    """

    def scroll_adaptive_to(self, widget: Widget):
        """
        Scrolls to specified widget if user didn't scroll up
        :param widget:
        :return:
        """
        if self.scroll_offset.y == self.max_scroll_y:
            widget.scroll_visible(duration=1)
