import os


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

"""
Function that deletes a directory
@param directory: Directory path
@return: None
"""
def delete_directory(directory):
    if os.path.exists(directory):
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                delete_directory(file_path)
        os.rmdir(directory)
