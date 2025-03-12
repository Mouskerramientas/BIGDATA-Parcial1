import os
from config import HTML_EXTENSION

"""
Function to check if the file has the HTML extension
@param file: Name of the file
@return: True if the file has the HTML extension, False otherwise
"""
def check_html_extension(file):
    return HTML_EXTENSION.match(file)

"""
Function to create a directory
@param directory: Name of the directory
@return: None
"""
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

"""
Exception for Not Found Errors in requests
Handles 404 errors
"""
class NotFoundException(Exception):
    """Custom Exception for Not Found Errors in requests"""
    def __init__(self, message):
        super().__init__(message)