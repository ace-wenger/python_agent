import os
from google import genai
from google.genai import types

def get_files_info(working_directory, directory = "."):
    try:

        dir_path = os.path.abspath(os.path.join(working_directory, directory))
        wd_path = os.path.abspath(working_directory)

        if os.path.commonpath([wd_path, dir_path]) != wd_path:
            #except Exceception as e:
            #    print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(dir_path):
            return f'Error: "{directory}" is not a directory'

        contents_path_list = [os.path.join(dir_path, name) for name in os.listdir(dir_path)]

        return "\n".join(list(map(get_file_details, list(map(os.path.abspath, contents_path_list)))))

    except Exception as e:
        return f"Error: {e}"

def get_file_details(file_path):
    file_name = file_path.rsplit("/",1)[1]
    file_size = os.path.getsize(file_path)
    isdir = os.path.isdir(file_path)
    
    return f'- {file_name}: file_size={file_size} bytes, is_dir={isdir}'

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

