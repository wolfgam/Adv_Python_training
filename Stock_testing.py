import dateutil.parser
import json
import os

import requests


class StockDataPoint():

    def __init__(self, symbol, timestamp, price):
        self.symbol = symbol
        self.timestamp = timestamp
        self.price = price

    def __eq__(self, other):
        return (self.symbol == other.symbol and
                self.timestamp == other.timestamp and
                self.price == other.price)

    def __repr__(self):
        return "#<symbol={0} timestamp={1} price={2}>".format(
            self.symbol, self.timestamp, self.price)


class YahooMock():

    def scrape(self, symbol):
        return ("PYPL", dateutil.parser.parse("2015-10-29T10:25:00.000"), 35.00)


class YahooReal():

    def scrape(self, symbol):
        url = "http://finance.yahoo.com/webservice/v1/symbols/{0}/quote?format=json".format(symbol)
        resp = requests.get(url)
        data = resp.json()
        info = data["list"]["resources"][0]["resource"]["fields"]
        timestamp = dateutil.parser.parse(info["utctime"])
        price = float(info["price"])
        return (symbol, timestamp, price)


def yahoo():
    if "ENV" in os.environ and os.environ["ENV"] == "test":
        return YahooMock()
    else:
        return YahooReal()


def scrape(symbol):
    symbol, timestamp, price = yahoo().scrape(symbol)
    return StockDataPoint(symbol, timestamp, price)


def historical(symbol, date_start, date_end):
    url = "http://query.yahooapis.com/v1/public/yql"
    query = '''select * from yahoo.finance.historicaldata where symbol = "{0}" and startDate = "{1}" and endDate = "{2}"'''.format(
        symbol, date_start, date_end)
    resp = requests.get(url, params={"q": query,
                                     "env": "http://datatables.org/alltables.env",
                                     "format": "json"})
    parsed_resp = resp.json()
    quotes = parsed_resp["query"]["results"]["quote"]
    return [StockDataPoint(symbol,
                           dateutil.parser.parse(quote["Date"]),
                           float(quote["Adj_Close"]))
            for quote in quotes]
