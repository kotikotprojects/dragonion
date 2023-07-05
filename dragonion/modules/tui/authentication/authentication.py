from textual.app import App, ComposeResult
from textual.widgets import Header
from textual.containers import Center
from .widgets.containers import LoginContainer


class LoginApp(App):
    DEFAULT_CSS = """
    LoginApp {
        layout: vertical;
        align-vertical: middle;
    }

    LoginContainer {
        align: center middle; 
        height: 1fr;
        max-width: 50%;
    }
    """

    def _on_compose(self) -> None:
        # noinspection PyTypeChecker
        self.title = 'd'

    def compose(self) -> ComposeResult:
        yield Header()
        yield Center(LoginContainer())


app = LoginApp()
