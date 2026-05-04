from src.ingestion.fetch_data import fetch_stock_data
from src.transformation.clean_data import clean_data
from src.loading.load_to_s3 import upload_to_s3

def run_pipeline(symbol):
    print('Starting pipeline.......')

    #Ingestion
    raw_data = fetch_stock_data(symbol)

    if not raw_data:
        print('No data found')
        return
    
    print(f'Fetched {len(raw_data)} records for symbol {symbol}')

    #transformation
    cleaned_data = clean_data(raw_data)
    print( f'Cleaned data contains {len(cleaned_data)} records after cleaning')

    #loading
    upload_to_s3(cleaned_data, 'stok-market-pipeline')

    print('Pipeline completed successfully')

if __name__ == "__main__":
    run_pipeline('AAPL')
