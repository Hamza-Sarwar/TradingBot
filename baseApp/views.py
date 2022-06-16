from django.shortcuts import render
from websocket import create_connection
import json, time
import pandas as pd
# Create your views here.

def index(request):

    # URL = "wss://ws-feed.pro.coinbase.com"
    # ws = create_connection(URL)

    # params = {"type": "subscribe", "product_ids": ["BTC-USD"],
    # "channels": ["heartbeat", {"name": "ticker", "product_ids": ["BTC-USD", "BTC-GBP"]}]}

    # ws.send(json.dumps(params))
    # while True:
    #     result = ws.recv()
    #     time.sleep(1)
    #     converted = json.loads(result)
    #     print(converted)
    return render(request, 'index.html', {})