import requests
import json
import dateutil.parser
from time import ctime
from pprint import pprint

#pip install dateutil

class StockDataPoint():
    def __init__(self,symbol, timestamp,price):
        self.symbol=symbol
        self.timestamp=timestamp
        self.price=price
        
    def __repr__(self):
        return "#<symbol={0} timestamp={1} price={2}>".format(self.symbol,self.timestamp,self.price)


def scrape(symbol):
    url = "http://finance.yahoo.com/webservice/v1/symbols/{0}/quote?format=json".format(symbol)
    resp = requests.get(url)
    data = resp.json()
    info = data["list"]["resources"][0]["resource"]["fields"]
    timestamp = dateutil.parser.parse(info["utctime"])
    price = float(info["price"])
    return StockDataPoint(symbol, timestamp, price)
