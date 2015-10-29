import dateutil.parser
import json
import os

import matplotlib.pyplot as plt
import mysql.connector
import numpy as np
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


class DataStoreReal():

    db_cxn = None

    def __init__(self):
        if not DataStoreReal.db_cxn:
            DataStoreReal.db_cxn = mysql.connector.connect(
                host="localhost", user="root", database="class")

    # schema:
    # create table prices (symbol text, timestamp datetime, price float)
    # create unique index prices_symbol_timestamp on prices (symbol (6), timestamp)

    def save(self, stock_data_points):
        cursor = DataStoreReal.db_cxn.cursor()
        for sdp in stock_data_points:
            cursor.execute('''insert into prices (symbol, timestamp, price) values (%s, %s, %s) on duplicate key update price=values(price)''',
                           (sdp.symbol, sdp.timestamp, sdp.price))
        DataStoreReal.db_cxn.commit()

    def load(self, symbol, date_start, date_end):
        cursor = DataStoreReal.db_cxn.cursor()
        cursor.execute('''select timestamp, price from prices where symbol = %s and timestamp >= %s and timestamp < %s''',
                       (symbol, date_start, date_end))
        return [StockDataPoint(symbol, timestamp, price) for (timestamp, price) in cursor]


def store():
    if "ENV" in os.environ and os.environ["ENV"] == "test":
        return DataStoreMock()
    else:
        return DataStoreReal()


def save(stock_data_points):
    store().save(stock_data_points)


def load(symbol, date_start, date_end):
    return store().load(symbol, date_start, date_end)


def plot_symbol(symbol, date_start, date_end):
    quotes = load(symbol, date_start, date_end)
    xs = np.array([quote.timestamp for quote in quotes])
    ys = np.array([quote.price for quote in quotes])
    plt.plot(xs, ys)
    plt.show()


def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


def plot_symbol_with_moving_avg(symbol, date_start, date_end):
    # Implement this.
    pass
