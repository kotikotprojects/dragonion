import asyncio

from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import Header, Static, LoadingIndicator
from textual.css.query import NoMatches


from .authentication import authentication
from .authentication.utils.results import ServiceAuthResult

from .identity import identity

from ..encryption.identity import Identity


class DragonionTuiApp(App):
    _pre_service_auth = None
    _pre_username = None
    service_auth = reactive(None)
    identity = reactive(None)

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

            if self._pre_username:
                self.mount(LoadingIndicator())
                self.identity = Identity(self._pre_username)
            else:
                self.mount(identity.IdentityWidget())

    async def watch_identity(self):
        if isinstance(self.identity, Identity):
            try:
                self.identity.generate()
                while self.identity.private_key is None:
                    await asyncio.sleep(0.1)
                await self.query_one(LoadingIndicator).remove()
            except NoMatches:
                pass

            if self.identity and self.service_auth:
                await self.mount(Static(str(self.identity)))
                await self.mount(Static(str(self.service_auth)))


app = DragonionTuiApp()
