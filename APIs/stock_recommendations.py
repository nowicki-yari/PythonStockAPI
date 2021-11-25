from flask_restful import Resource
import yfinance as yf
import pandas as pd


class StockRecommendations(Resource):
    def get(self, stock, start_date, end_date):
        info = yf.Ticker(stock)
        df = info.recommendations.reset_index()
        df = df[(df['Date'] > start_date) & (df['Date'] < end_date)]
        return df.to_json(date_format='iso')