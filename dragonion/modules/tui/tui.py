from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import Header, Static
from textual.css.query import NoMatches


from .authentication import authentication
from .authentication.utils.results import ServiceAuthResult


class DragonionTuiApp(App):
    _pre_service_auth = None
    service_auth = reactive(None)

    def compose(self) -> ComposeResult:
        yield Header()
        if not self._pre_service_auth:
            yield authentication.LoginWidget()

    def _on_compose(self) -> None:
        if self._pre_service_auth is not None:
            self.service_auth = self._pre_service_auth

    def watch_service_auth(self):
        if isinstance(self.service_auth, ServiceAuthResult):
            try:
                self.query_one(authentication.LoginWidget).remove()
            except NoMatches:
                pass

            self.mount(Static(str(self.service_auth)))


app = DragonionTuiApp()
