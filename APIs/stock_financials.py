from flask_restful import Resource
import yfinance as yf
import os


class StockFinancials(Resource):
    def get(self, stock, key):
        if key == os.environ['Stock_API']:
            info = yf.Ticker(stock)
            return info.financials.transpose().iloc[-1].to_json(date_format='iso')
        return {'error': 'invalid key'}
