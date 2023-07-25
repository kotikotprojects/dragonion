from dragonion.modules.tui.chat.widgets.containers import MessagesContainer

import websockets.exceptions

from dragonion_core.proto.web.webmessage import (
    WebMessage,
    WebConnectionMessage,
    WebDisconnectMessage,
    WebMessageMessage,
    WebNotificationMessage,
    WebErrorMessage
)
from dragonion.modules.tui.chat.widgets.items.message import Message

from datetime import datetime


def render_time():
    return f"[#a5abb3][{datetime.now().time().strftime('%H:%M:%S')}][/]"


async def handle_websocket():
    from dragonion.modules.tui import app

    container = app.query_one(MessagesContainer)

    async for message in app.user_storage.websocket:
        try:
            webmessage = WebMessage.from_json(message)

            match webmessage.type:
                case "connect":
                    webmessage: WebConnectionMessage
                    app.user_storage.keys |= {
                        webmessage.username: webmessage.public_key
                    }
                    container.write(
                        f"- Connected {webmessage.username} - {render_time()}"
                    )
                case "disconnect":
                    webmessage: WebDisconnectMessage
                    container.write(
                        f"- Disconnected {webmessage.username} - "
                        f"{render_time()}"
                    )
                case "message":
                    webmessage: WebMessageMessage
                    if not container.last_message or \
                            container.last_message.author != webmessage.username:
                        container.mount_scroll_adaptive(
                            Message(
                                avatar=webmessage.avatar,
                                message=webmessage.decrypt(app.identity),
                                author=webmessage.username
                            )
                        )
                    else:
                        container.last_message.add_message(
                            message=webmessage.decrypt(app.identity)
                        )
                case "notification":
                    webmessage: WebNotificationMessage
                    container.write(
                        f"[blue]- {webmessage.message} - {render_time()}[/]"
                    )
                case "error":
                    webmessage: WebErrorMessage
                    container.write(
                        f"[red]- {webmessage.error_message} - "
                        f"{render_time()}[/]"
                    )

        except websockets.exceptions.ConnectionClosedOK:
            pass
        except websockets.exceptions.ConnectionClosed:
            container.write(
                f"[bold red]Disconnected[/], consider rejoining"
            )
        except Exception as e:
            container.write(f'[red]Error {e.__class__}[/] in message handler: {e}')
