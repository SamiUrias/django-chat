from channels.routing import route
from chat.consumers import ws_add, ws_message, ws_disconnect
# In routing.py
from channels.routing import route

channel_routing = [
    route("http.request", "chat.consumers.http_consumer"),
    route("websocket.connect", ws_add),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
]