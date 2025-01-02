import ast
import json
import sys

# Function to find functions defined but never invoked
def find_uninvoked_functions(script: str) -> list:
    try:
        tree = ast.parse(script)

        # Collect all function definitions
        defined_functions = {node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)}

        # Collect all function calls
        called_functions = {node.func.id for node in ast.walk(tree)
                            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)}

        # Find functions that are defined but never called
        if len(defined_functions) >1:
            uninvoked_functions = defined_functions - called_functions
        else:
            uninvoked_functions = []
        return list(uninvoked_functions)
    except Exception as e:
        return []  # Return empty list if the script cannot be parsed

# Main function to process the JSON file
def process_json(file_path: str):
    try:
        # Read the JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Track items where functions are defined but not invoked
        uninvoked_items = []

        for item in data:
            uninvoked_functions = find_uninvoked_functions(item.get("generated_code", ""))
            if len(uninvoked_functions) > 0:  # If there are uninvoked functions
                uninvoked_items.append(f'{item["task_id"]}_{item["model"]}')

        # Print task IDs of items with uninvoked functions
        print("Task IDs with uninvoked functions:")
        for task_id in uninvoked_items:
            print(task_id)
    except Exception as e:
        print(f"Error processing the JSON file: {e}")

# Entry point
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_json_file>")
    else:
        process_json(sys.argv[1])
