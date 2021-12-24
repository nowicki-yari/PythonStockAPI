# coding=utf-8
import os
from flask import Flask
from flask_restful import Api
from APIs.stock_info import StockInfo
from APIs.stock_historic_data import StockHistoricData
from APIs.stock_historic_data import StockHistoricDataLatest
from APIs.stock_dividends import StockDividends
from APIs.stock_financials import StockFinancials
from APIs.stock_recommendations import StockRecommendations
from APIs.stock_recommendations import StockRecommendationsLatest
from APIs.stock_institutional_holders import StockInstitutionalHolders
from flask_cors import CORS

os.environ['Stock_API'] = '2e60b5c63eb37f3d1e6143be7d6c3eb6'

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(StockInfo, '/stock/<string:stock>/info/<string:key>')
api.add_resource(StockDividends, '/stock/<string:stock>/dividends/<string:key>')
api.add_resource(StockFinancials, '/stock/<string:stock>/financials/<string:key>')
api.add_resource(StockInstitutionalHolders, '/stock/<string:stock>/institutional_holders/<string:key>')

api.add_resource(StockHistoricDataLatest, '/stock/<string:stock>/history/<string:key>')
api.add_resource(StockHistoricData, '/stock/<string:stock>/history/<string:start_date>/<string:end_date>/<string:key>')

api.add_resource(StockRecommendationsLatest, '/stock/<string:stock>/recommendations/<string:start_date>/<string:key>')
api.add_resource(StockRecommendations, '/stock/<string:stock>/recommendations/<string:start_date>/<string:end_date>/<string:key>')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
