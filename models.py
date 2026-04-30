from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class StockData(db.Model):
    __tablename__ = 'stock_data'

    id = db.Column(db.Integer , primary_key = True)

    #stock identifier
    symbol = db.Column(db.String(10), nullable=False)

    #date of stock data
    date = db.Column(db.Date , nullable=False)

    #price data
    open = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    close = db.Column(db.Float)

    #trading values
    volume = db.Column(db.BigInteger)

    #helper method(used later for API response)
    def to_dict(self):
        return {
            'symbol':self.symbol,
            'date': self.date,
            'open': self.open,
            'high': self.high,
            'low' : self.low,
            'close': self.close,
            'volume': self.volume
        }