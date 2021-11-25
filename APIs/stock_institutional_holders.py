from flask_restful import Resource
import yfinance as yf


class StockInstitutionalHolders(Resource):
    def get(self, stock):
        info = yf.Ticker(stock)
        return info.institutional_holders.to_json()