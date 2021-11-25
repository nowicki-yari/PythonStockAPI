from flask_restful import Resource
import yfinance as yf
import pandas as pd


class StockFinancials(Resource):
    def get(self, stock):
        info = yf.Ticker(stock)
        return info.financials.transpose().to_json()