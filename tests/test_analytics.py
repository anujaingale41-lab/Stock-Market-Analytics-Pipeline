import pytest
from services.analytics import calculate_analytics

class MockStock:
    def __init__(self,close):
        self.close = close

def test_return_positive():
    stock_data = [MockStock(100), MockStock(110), MockStock(120)]
    result = calculate_analytics(stock_data)
    assert abs(result['return'] - (20)) < 0.01

def test_return_negative():
    stock_data = [MockStock(120), MockStock(110), MockStock(100)]
    result = calculate_analytics(stock_data)
    assert abs(result['return'] - (-20)) < 0.01

def test_max_drawdown():
    stock_data = [MockStock(100), MockStock(120), MockStock(80), MockStock(90)]
    result = calculate_analytics(stock_data)
    assert abs(result['max_drawdown'] - (33.33)) < 0.5

def test_volatility_is_non_negative():
    stock_data = [MockStock(100), MockStock(105), MockStock(102), MockStock(108)]
    result = calculate_analytics(stock_data)
    assert result['volatility'] >= 0

def test_single_record_return_zero():
    stock_data = [MockStock(100)]
    result = calculate_analytics(stock_data)
    assert result['return'] == 0