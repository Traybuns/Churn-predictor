import boto3
import pandas as pd

def ingest_data(bucket_name, file_key):
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    data = pd.read_csv(obj['Body'])
    return data

if __name__ == "__main__":
    data = ingest_data('my-churn-bucket', 'data.csv')
    print("Data Ingested:", data.head())
