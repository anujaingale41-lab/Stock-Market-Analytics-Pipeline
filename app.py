import os

from flask import Flask, request
from numpy import select
from models import StockData, db
from config import DB_URI
from src.ingestion.fetch_data import fetch_stock_data
from datetime import datetime
from services.analytics import calculate_analytics
from src.transformation import clean_data

app = Flask(__name__)

#connect to PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

#Initialise DB
db.init_app(app)

#Create tables automatically
with app.app_context():
    db.create_all()

#test route
@app.route("/")
def home():
    return {'message': 'Stock Market Pipeline Running'}


@app.route('/fetch-stock')
def fetch_stock():

    symbol = request.args.get('symbol')
    if not symbol:
        return{'error':'Please provide stock symbol'}, 400

    try:
        data = fetch_stock_data(symbol)
    except Exception as e:
        return {'error': str(e)}, 500   
    
    if not data:
        return {'error':'API failed or limit reached'},500


    cleaned_data = clean_data(data)
    for item in cleaned_data:
        stock= StockData(
            symbol=item['symbol'],
            date=datetime.strptime(item['date'],'%Y-%m-%d').date(),
            open=item['open'],
            high=item['high'],
            low=item['low'],
            close=item['close'],
            volume=item['volume']
        )
        db.session.add(stock)
    db.session.commit()

    return{'message':f'Data for {symbol} stored successfully'}

@app.route('/analytics')
def analytics():

    symbol = request.args.get('symbol')

    if not symbol:
        return {'error':'Please provide stock symbol'},400
    
    data = db.session.execute(select(StockData).where(StockData.symbol == symbol).order_by(StockData.date)).scalars().all()

    if not data:
         return {'error':' No data found'}, 404
    
    result = calculate_analytics(data)
    result['symbol']= symbol
    return result
    
#run server
if __name__=='__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 't'])