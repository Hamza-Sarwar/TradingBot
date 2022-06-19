import json
from tarfile import RECORDSIZE
from time import sleep
from websocket import create_connection
from channels.generic.websocket import WebsocketConsumer

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        URL = "wss://ws-feed.pro.coinbase.com"
        ws = create_connection(URL)
        params = {
            "type": "subscribe",
            "product_ids": ["BTC-USD", "ETH-USD", "ADA-USD", "SOL-USD", "DOT-USD"],
            "channels": ["ticker"]
            }
        ws.send(json.dumps(params))
        while True:
            result = ws.recv()
            sleep(1)
            record = result.split(',')[2:8]
            
            if len(record) != 6:
                del record
            else:
                #print(f"{record} size:{len(record)} ")
                eth = {
                'type': record[0][14:-1],
                'price': record[1][9:-1],
                'open_24h': record[2][12:-1],
                'volume_24h': record[3][14:-1],
                'low_24h': record[4][11:-1],
                'high_24h': record[5][12:-1]
                }
                self.send(json.dumps(eth))

                   


