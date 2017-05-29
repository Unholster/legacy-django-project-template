"""
    YOUR DJANGO_CHANNELS CONSUMERS HERE
"""
from channels.handler import AsgiHandler
from django.http import HttpResponse


def http_consumer(message):
    # Make standard HTTP response - access ASGI path attribute directly
    response = HttpResponse(f"Hello world! You asked for {message.content['path']}")
    # Encode that response into message format (ASGI)
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)
