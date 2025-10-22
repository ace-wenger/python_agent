import os
from config import MAX_CHARS
from google import genai
from google.genai import types

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

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read file contents limited to 10,000 characters, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to be read, relative to the working directory",
            ),
        },
    ),
)
