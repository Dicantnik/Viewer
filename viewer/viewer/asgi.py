
# import os
# from rooms.routing import websocket_urlpatterns
# from django.core.asgi import get_asgi_application
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter

# django_asgi_app = get_asgi_application()
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "viewer.settings")

# application = ProtocolTypeRouter({
#     'http': django_asgi_app, 
#     # 'websocket': AuthMiddlewareStack(
#     #     URLRouter(
#     #        websocket_urlpatterns
#     #     )
#     # )
# })


import os

from rooms import routing
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import ProtocolTypeRouter, URLRouter


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'viewer.settings')
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket': AllowedHostsOriginValidator(AuthMiddlewareStack(
        URLRouter(
           routing.websocket_urlpatterns
        )
    ) )   
    # Just HTTP for now. (We can add other protocols later.)
})
