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

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(StockInfo, '/stock/<string:stock>/info')
api.add_resource(StockDividends, '/stock/<string:stock>/dividends')
api.add_resource(StockFinancials, '/stock/<string:stock>/financials')
api.add_resource(StockInstitutionalHolders, '/stock/<string:stock>/institutional_holders')

api.add_resource(StockHistoricDataLatest, '/stock/<string:stock>/history')
api.add_resource(StockHistoricData, '/stock/<string:stock>/history/<string:start_date>/<string:end_date>')

api.add_resource(StockRecommendationsLatest, '/stock/<string:stock>/recommendations/<string:start_date>')
api.add_resource(StockRecommendations, '/stock/<string:stock>/recommendations/<string:start_date>/<string:end_date>')


if __name__ == '__main__':
    app.run()
