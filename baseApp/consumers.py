import json
from time import sleep
from random import randint
from websocket import create_connection
from channels.generic.websocket import WebsocketConsumer

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        URL = "wss://ws-feed.pro.coinbase.com"
        ws = create_connection(URL)

        params = {"type": "subscribe", "product_ids": ["BTC-USD"],
        "channels": ["heartbeat", {"name": "ticker", "product_ids": ["BTC-USD", "BTC-GBP"]}]}

        ws.send(json.dumps(params))
        while True:
            result = ws.recv()
            sleep(1)
            self.send(json.dumps({
                'message': result
            }))

        # for i in range(1000):
        #     self.send(json.dumps({'message': randint(1,1000)}))
        #     sleep(1)

