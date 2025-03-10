from datetime import date
import os
import boto3
from botocore.exceptions import ClientError
from bs4 import BeautifulSoup
import csv

def extract_info(html_content, curr_date):
    soup = BeautifulSoup(html_content, 'html.parser')
    data = []

    for house in soup.find_all("a", class_="listing listing-card"):
        valor = house.get("data-price")
        barrio = house.get("data-location")
        num_habitaciones = house.get("data-rooms")
        mts2 = house.get("data-floorarea")
        # Extraer los baños
        num_banos = 0
        banos_tag = house.find("p", {"data-test": "bathrooms"})
        if banos_tag:
            num_banos = banos_tag.text.strip().split()[0]  # Extrae solo el número
        data.append([curr_date, barrio, valor, num_habitaciones, num_banos, mts2])

    return data

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['FechaDescarga', 'Barrio', 'Valor', 'NumHabitaciones', 'NumBanos', 'mts2'])
        writer.writerows(data)

def upload_file(file_name, bucket, object_name=None):

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        print(f"✅ Archivo '{file_name}' subido correctamente al bucket '{bucket}' con nombre '{object_name}'")
    except ClientError as e:
        print(f"❌ Error al subir el archivo '{file_name}' al bucket '{bucket}' con nombre '{object_name}': {e}")
        return False
    return True


def main():
    curr_date = date.today().strftime("%Y-%m-%d")
    os.makedirs(f"casas-final-{curr_date}", exist_ok=True)
    with open('landing-casas-2025-03-09/001.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    data = extract_info(html_content, curr_date)
    save_to_csv(data, 'casas-final-2025-03-09/001.csv')
    upload_file('casas-final-2025-03-09/001.csv', 'bucker-zappa-downloder-storage')

if __name__ == '__main__':
    main()
