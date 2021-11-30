from flask_restful import Resource
import yfinance as yf
import datetime


class StockHistoricData(Resource):
    def get(self, stock, start_date, end_date):
        data = yf.download(stock, start=start_date, end=end_date)
        data = data.reset_index()
        return data.transpose().to_json(date_format='iso')


class StockHistoricDataLatest(Resource):
    def get(self, stock, start_date):
        print(datetime.date.today())
        data = yf.download(stock, start=start_date, end=str(datetime.date.today()))
        data = data.reset_index()
        return data.transpose().to_json(date_format='iso')