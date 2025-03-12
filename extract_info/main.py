from datetime import date
from html_extracter import get_html_code
from utils import NotFoundException, create_directory
from parser import extract_and_parse_info
from files import save_to_csv, upload_file


"""
Main function to run the program
@param record: Record with the information of the file
@return: None
"""
def main(record):

    file_name = record["s3"]["object"]["key"]
    bucket_name = record['s3']['bucket']['name']

    html_content = get_html_code(file_name, bucket_name)
    
    if not html_content:
        raise NotFoundException("El archivo no es un HTML")

    curr_date = date.today().strftime("%Y-%m-%d")
    
    create_directory(f"/tmp/casas-final-{curr_date}")

    data = extract_and_parse_info(html_content, curr_date)

    file_name_split = str(file_name.split("/")[1]).replace(".html", "")

    csv_file_name = f'/tmp/casas-final-{curr_date}/{file_name_split}.csv'

    save_to_csv(csv_file_name, data)

    upload_file(csv_file_name)
