from flask_restful import Resource
import yfinance as yf
from datetime import date, datetime, timedelta
import os


class StockHistoricData(Resource):
    def get(self, stock, start_date, end_date, key):
        if key == os.environ['Stock_API']:
            data = yf.download(stock, start=start_date, end=end_date)
            data = data.reset_index()
            return data.transpose().to_json(date_format='iso')
        return {'error': 'invalid key'}


class StockHistoricDataLatest(Resource):
    def get(self, stock, key):
        if key == os.environ['Stock_API']:
            year_before = date.today() - timedelta(days=365)
            data = yf.download(stock, start=str(year_before), end=str(date.today()))
            data = data.reset_index()
            return data.transpose().to_json(date_format='iso')
        return {'error': 'invalid key'}
