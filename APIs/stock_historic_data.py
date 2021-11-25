from flask_restful import Resource
import yfinance as yf


class StockHistoricData(Resource):
    def get(self, stock, start_date, end_date):
        data = yf.download(stock, start=start_date, end=end_date)
        data = data.reset_index()
        return data.transpose().to_json(date_format='iso')
