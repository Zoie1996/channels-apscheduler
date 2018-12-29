from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import data.routing

'''
ProtocolTypeRouter将首先检查连接类型。如果是WebSocket连接（ws：//或wss：//），
则将连接到AuthMiddlewareStack
'''

application = ProtocolTypeRouter({
    # (http->django views is added by default)

    'websocket': AuthMiddlewareStack(
        URLRouter(
            data.routing.websocket_urlpatterns
        )
    ),
})
