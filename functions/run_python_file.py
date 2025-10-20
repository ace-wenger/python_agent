import subprocess
import os

def run_python_file(working_directory, file_path, args=[]):
    try:
        path = os.path.abspath(os.path.join(working_directory, file_path))
        wd_path = os.path.abspath(working_directory)

        if os.path.commonpath([wd_path, path]) != wd_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'    
        if not os.path.exists(path):
            return f'Error: File "{file_path}" not found.'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        command = ["python", os.path.basename(file_path)]
        
        if len(args) > 0: 
            for arg in args:
                command.append(arg)

        file_result = subprocess.run(
            args=command,
            cwd=wd_path,
            capture_output=True, 
            timeout=30
        )

        if file_result.returncode != 0:
            return f'Process exited with code {file_result.returncode}'

        elif not file_result.stdout and not file_result.stderr:
            return f'No output produced'

    except Exception as e:
        return f'Error: executing Python file: {e}'

    return f'STDOUT: {file_result.stdout} STDERR: {file_result.stderr}'
