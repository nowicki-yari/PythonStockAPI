from flask_restful import Resource, reqparse
import yfinance as yf
import pandas as pd
import os


class StockInfo(Resource):
    def get(self, stock, key):
        if key == os.environ['Stock_API']:
            info = yf.Ticker(stock)
            return pd.DataFrame.from_dict(info.info, orient='index').to_json()
        return {'error': 'invalid key'}



