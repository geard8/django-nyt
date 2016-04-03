# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from channels.routing import route

from . import consumers

channel_routing = [
    route("websocket.connect", consumers.ws_connect),
    route("websocket.disconnect", consumers.ws_disconnect),
]
