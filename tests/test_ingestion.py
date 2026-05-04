from src.ingestion.fetch_data import fetch_stock_data

def test_fetch_stock_data():
    symbol = 'AAPL'
    data = fetch_stock_data(symbol)

    assert data is not None, "Data should not be None"
    assert isinstance(data, list), "Data should be a list"
    assert len(data) > 0, "Data list should not be empty"

    for item in data:
        assert 'symbol' in item, "Each item should have a 'symbol' key"
        assert 'date' in item, "Each item should have a 'date' key"
        assert 'open' in item, "Each item should have an 'open' key"
        assert 'high' in item, "Each item should have a 'high' key"
        assert 'low' in item, "Each item should have a 'low' key"
        assert 'close' in item, "Each item should have a 'close' key"
        assert 'volume' in item, "Each item should have a 'volume' key"
        