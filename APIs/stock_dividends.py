from flask_restful import Resource
import yfinance as yf
import pandas as pd


class StockDividends(Resource):
    def get(self, stock):
        info = yf.Ticker(stock)
        df = info.dividends.to_frame().reset_index()
        df = df.iloc[::-1]
        df = df.reset_index(drop=True)
        return df.to_json(date_format='iso')