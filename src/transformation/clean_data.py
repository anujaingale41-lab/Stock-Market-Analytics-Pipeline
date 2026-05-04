from datetime import datetime

def clean_data(data):
    cleaned_data = []
    for item in data:
        try:
            cleaned_item = {
                'symbol': item['symbol'],
                'date': datetime.strptime(item['date'], '%Y-%m-%d').date(),
                'open': float(item['open']),
                'high': float(item['high']),
                'low': float(item['low']),
                'close': float(item['close']),
                'volume': int(item['volume'])
            }

            #basic validation
            if cleaned_item['open'] < 0 or cleaned_item['high'] < 0 or cleaned_item['low'] < 0 or cleaned_item['close'] < 0 or cleaned_item['volume'] < 0:
                print(f"Invalid data values for item {item}")
                continue
            cleaned_data.append(cleaned_item)
        except (ValueError, KeyError) as e:
            print(f"Data cleaning error for item {item}: {e}")
            continue
    return cleaned_data