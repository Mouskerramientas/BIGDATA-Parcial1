import boto3
from utils import check_html_extension

"""

"""
def fetch_html_content(file: str, bucket_name: str):
    
    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket=bucket_name, Key=file)
    html_content = response['Body'].read().decode('utf-8')

    return html_content

"""

"""
def get_html_code(file: str, bucket: str):

    if not check_html_extension(file): return None
    
    html_code = fetch_html_content(file, bucket)

    return html_code
