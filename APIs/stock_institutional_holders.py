import os
from flask_restful import Resource
import yfinance as yf


class StockInstitutionalHolders(Resource):
    def get(self, stock, key):
        if key == os.environ['Stock_API']:
            info = yf.Ticker(stock)
            return info.institutional_holders.to_json()
        return {'error': 'invalid key'}