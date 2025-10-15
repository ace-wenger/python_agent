import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        path = os.path.abspath(os.path.join(working_directory, file_path))
        wd_path = os.path.abspath(working_directory)

        if os.path.commonpath([wd_path, path]) != wd_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(path, 'r') as f:
            file_data = f.read(MAX_CHARS)

        if len(file_data) == MAX_CHARS:
            return f'{file_data} [...File "{file_path}" truncated at {MAX_CHARS} characters]'
        
        return file_data

    except Exception as e:
            return f'Error: {e}'
