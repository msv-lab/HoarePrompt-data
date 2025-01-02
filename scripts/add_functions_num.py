import ast
import json
import sys

# Function to count functions in a Python script
def count_functions(script: str) -> int:
    try:
        tree = ast.parse(script)
        return sum(isinstance(node, ast.FunctionDef) for node in ast.walk(tree))
    except Exception:
        return 0  # Return 0 if the script cannot be parsed

# Main function to process the JSON file
def process_json(file_path: str):
    try:
        # Read the JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Add the 'functions' field to each item
        for item in data:
            item['functions'] = count_functions(item.get("generated_code", ""))
        
        # Write the updated JSON back to the same file
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        
        print(f"Processed JSON successfully written to {file_path}")
    except Exception as e:
        print(f"Error processing the JSON file: {e}")

# Entry point
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_json_file>")
    else:
        process_json(sys.argv[1])
