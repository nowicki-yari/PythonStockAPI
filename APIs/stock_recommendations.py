import os
from flask_restful import Resource
import yfinance as yf
import datetime


class StockRecommendations(Resource):
    def get(self, stock, start_date, end_date, key):
        if key == os.environ['Stock_API']:
            info = yf.Ticker(stock)
            df = info.recommendations.reset_index()
            df = df[(df['Date'] > start_date) & (df['Date'] < end_date)]
            df = df.iloc[::-1]
            df = df.reset_index(drop=True)
            return df.to_json(date_format='iso')
        return {'error': 'invalid key'}


class StockRecommendationsLatest(Resource):
    def get(self, stock, start_date, key):
        if key == os.environ['Stock_API']:
            info = yf.Ticker(stock)
            df = info.recommendations.reset_index()
            df = df[(df['Date'] > start_date) & (df['Date'] < str(datetime.date.today()))]
            df= df.iloc[::-1]
            df = df.reset_index(drop=True)
            return df.to_json(date_format='iso')
        return {'error': 'invalid key'}