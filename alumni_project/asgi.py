"""
ASGI config for alumni_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

import os
from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# import alumni_app.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alumni_project.settings")

application = get_asgi_application()
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             alumni_app.routing.websocket_urlpatterns
#         )
#     ),
# })