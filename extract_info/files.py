import csv
import boto3

from config import CSV_BUCKET_NAME


"""
Function to write the data to a CSV file
@param data: List with the data to write
@param filename: Name of the file to write
@return: None
"""
def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ['FechaDescarga', 'Barrio', 'Valor', 'NumHabitaciones', 'NumBanos', 'mts2']
        )
        writer.writerows(data)
"""
Function to upload a file to an S3 bucket
@param file_name: Name of the file to upload
@param bucket: Name of the bucket
@param object_name: Name of the object in the bucket
@return: None
"""
def upload_file(file_name, bucket=CSV_BUCKET_NAME, object_name=None):

    object_name = file_name.replace("/tmp/","")

    # Upload the file
    s3_client = boto3.client('s3')
    s3_client.upload_file(file_name, bucket, object_name)
    print(f"✅ Archivo '{object_name}' subido correctamente al bucket '{bucket}''")
