import os
from google import genai
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        path = os.path.abspath(os.path.join(working_directory, file_path))
        wd_path = os.path.abspath(working_directory)

        if os.path.commonpath([wd_path, path]) != wd_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "w") as f:
            f.write(content)

    except Exception as e:
            return f'Error: {e}'

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes file with provided content, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to be written, relative to the working directory",
            ),
            "content": types.Schema( 
                type=types.Type.STRING,
                description="The contents of the written file."
            ),
        },
    ),
)
