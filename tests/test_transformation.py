from src.transformation.clean_data import clean_data

def test_clean_data():
    sample = [{
        'symbol': 'AAPL',
        'date': '2025-01-01',
        'open': '150.00',
        'high': '155.00',       
        'low': '149.00',
        'close': '154.00',  
        'volume': '1000000'
    }]

    result = clean_data(sample)

    assert isinstance(result ,list)
    assert len(result) ==1
    assert result[0]["open"] == 150.00
     