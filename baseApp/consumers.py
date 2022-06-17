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

        params = {
            "type": "subscribe",
            "product_ids": ["BTC-USD", "ETH-USD"],
            "channels": ["ticker"]
            }

        ws.send(json.dumps(params))
        while True:
            result = ws.recv()
            sleep(1)
            if (result.find("ETH-USD") != -1):

                print(result)
            else:
                print("Not here")
            # record = result.split(',')[3:8]
            # if len(record) != 5:
            #     del record
            # else:

            #     print(f"{record} size:{len(record)} ")
                # self.send(json.dumps({
                #     'price': record[0][9:-1],
                #     'open_24h': record[1][12:-1],
                #     'volume_24h': record[2][14:-1],
                #     'low_24h': record[3][11:-1],
                #     'high_24h': record[4][12:-1]
                # }))

        # for i in range(1000):
        #     self.send(json.dumps({'message': randint(1,1000)}))
        #     sleep(1)

