import requests
import os
from dotenv import load_dotenv


#load variable from .env
load_dotenv()
API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')


def fetch_stock_data(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

    try:
        response = requests.get(url, timeout = 10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print('Error fetching stock data:', e)
        return None
    except requests.exceptions/TimeoutError:
        print('Request timed out while fetching stock data')
        return None

    data = response.json()

    if "Time Series (Daily)" not in data:
        print('API error:', data.get("Error Message", "Unknown error"))
        return None
    
    time_series = data["Time Series (Daily)"]

    result=[]

    for date,value in time_series.items():
        stock_entry = {
            'symbol': symbol,
            'date': date,
            'open':  float(value["1. open"]),
            'high': float(value['2. high']),
            'low': float(value['3. low']),
            'close': float(value['4. close']),
            'volume': int(value['5. volume'])
        }
        result.append(stock_entry)

    return result