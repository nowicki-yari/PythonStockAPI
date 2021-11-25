from flask_restful import Resource
import yfinance as yf
import pandas as pd


class StockInfo(Resource):
    def get(self, stock):
        info = yf.Ticker(stock)
        return pd.DataFrame.from_dict(info.info, orient='index').to_json()



