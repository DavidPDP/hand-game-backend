from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from django.conf.urls import url
from match_gestor.consumer import MatchConsumer

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    url(r"^match/(?P<username>[\w.@+-]+)/(?P<usertype>[\w.@+-]+)$", MatchConsumer),
                ]
            )
        )
    )
})