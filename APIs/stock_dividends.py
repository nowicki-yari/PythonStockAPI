from flask_restful import Resource
import yfinance as yf
import pandas as pd


class StockDividends(Resource):
    def get(self, stock):
        info = yf.Ticker(stock)
        return info.dividends.to_frame().to_json()