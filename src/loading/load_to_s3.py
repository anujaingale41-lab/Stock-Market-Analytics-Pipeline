import boto3
import pandas as pd
from datetime import datetime
import os

def upload_to_s3(data, busket_name):

    if not data:
        print('No data to upload')
        return
    
    df=pd.DataFrame(data)

    file_name = "stock_data.csv"

    df.to_csv(file_name, index=False)

    s3= boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_REGION')
    )


    today = datetime.now().strftime("%Y-%m-%d")

    s3_key = f"stock_data/{today}/{file_name}"

    s3.upload_file(file_name, busket_name, s3_key)
    print(f"File uploaded to S3 at {s3_key}")

    
