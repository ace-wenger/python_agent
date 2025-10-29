import google
from google import genai 
from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    function_args = function_call_part.args
    function_args["working_directory"] = "./calculator"

    functions = {
        "write_file": write_file,
        "get_files_info": get_files_info,
        "run_python_file": run_python_file,
        "get_file_content": get_file_content,
    }
    
    if not function_name in functions:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    
    if verbose:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    result = functions[function_name](**function_args)

    return types.Content(
        role = "tool",
        parts = [
            types.Part.from_function_response(
                name = function_name,
                response = {"result": result},
            )
        ],
    )

