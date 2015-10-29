import datetime

from stocks import scrape, StockDataPoint

def test_scrape():
    assert scrape("PYPL") == StockDataPoint("PYPL",
                                            datetime.datetime(2015, 10, 29, 10, 25),
                                            35.00)
