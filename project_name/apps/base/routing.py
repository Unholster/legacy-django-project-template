"""
    YOUR DJANGO_CHANNELS ROUTERS HERE
"""
from channels import route
from channels.handler import AsgiHandler
from django.http import HttpResponse

channel_routing = [
    route('websocket.receive', '{{project_name}}.apps.base.consumers.http_consumer'),
]


def http_consumer(message):
    # Make standard HTTP response - access ASGI path attribute directly
    response = HttpResponse(f"Hello world! You asked for {message.content['path']}")
    # Encode that response into message format (ASGI)
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)
