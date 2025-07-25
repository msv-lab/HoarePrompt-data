import json
import ast
from pathlib import Path

def load_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def save_data(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def find_loop_depth(node, current_depth=0):
    if isinstance(node, (ast.For, ast.While)):
        current_depth += 1
        max_depth = current_depth
        for child in ast.iter_child_nodes(node):
            max_depth = max(max_depth, find_loop_depth(child, current_depth))
        return max_depth
    else:
        max_depth = current_depth
        for child in ast.iter_child_nodes(node):
            max_depth = max(max_depth, find_loop_depth(child, current_depth))
        return max_depth

def calculate_depth_for_programs(data):
    for entry in data:
        try:
            code = entry.get("generated_code", "")
            tree = ast.parse(code)
            entry["nested_loop_depth"] = find_loop_depth(tree)
        except Exception as e:
            entry["nested_loop_depth"] = -1  # Assign -1 if parsing fails
    return data


#write a function to remove all rows with depth different than 1 or 2 
def remove_outliers(data):
    return [entry for entry in data if entry["nested_loop_depth"] in [1, 2]]

# Hardcoded file paths
data_folder = Path("/home/dimitris/HoarePrompt-data/PilotData/data")
input_file = data_folder / "code_force_2024.json"
output_file = data_folder / "code_force_2024_depth.json"

# Load the data
data = load_data(input_file)

# Calculate loop depth
print(f"original loop depth for {len(data)} programs")
data_with_depth = calculate_depth_for_programs(data)
data_with_depth = remove_outliers(data_with_depth)
print(f"Found loop depth for {len(data_with_depth)} programs")

# Save the updated data
save_data(data_with_depth, output_file)

print(f"Updated data with loop depth saved to {output_file}")
