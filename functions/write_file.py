import os

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
