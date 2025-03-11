import boto3
from config import HTML_BUCKET_NAME
from api_requests import fetch_page

"""
Function that downloads a number of pages from the Mitula URL
@param num_pages: Number of pages to download
@return: List of HTML pages
"""
def download_pages(dir_path: str, num_pages: int):

    pages = []

    for i in range(1, num_pages + 1):
        pages.append({
            "file_name": f"{dir_path}/{i:03}.html",
            "content": fetch_page(i)
        })

    return pages

"""
Function that downloads and saves a number of pages from the Mitula URL
@param num_pages: Number of pages to download
@return: List of file names
"""
def download_and_save_pages(dir_path: str, num_pages: int = 10):
    pages = download_pages(dir_path, num_pages)

    for page in pages:
        with open(page["file_name"], "w") as file:
            file.write(page["content"])

    return [page["file_name"] for page in pages]

"""
Function that uploads a page to the S3 bucket
@param file_name: File name
@return: None
"""
def upload_page(file_name: str):

    object_name = file_name.replace("/tmp/", "")

    s3_client = boto3.client('s3')
    
    s3_client.upload_file(file_name, HTML_BUCKET_NAME, object_name)

    print(f"✅ Archivo '{object_name}' subido correctamente al bucket '{HTML_BUCKET_NAME}'")

"""
Function that uploads a list of pages to the S3 bucket
@param files_names: List of file names
@return: None
"""
def upload_pages_to_s3(files_names: list[str]):
    [upload_page(file_name) for file_name in files_names]
