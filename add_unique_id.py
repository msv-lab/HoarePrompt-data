import json

def add_unique_ids_to_json_list(json_file, output_file):
    """
    Reads a JSON file containing a list of dictionaries, adds a `unique_id` field to each dictionary
    (concatenating `task_id` and `model`), and writes the updated JSON list to a new file.
    """
    try:
        # Load the JSON data from the file
        with open(json_file, 'r') as file:
            data = json.load(file)

        # Ensure it's a list
        if not isinstance(data, list):
            print("Error: JSON data is not a list.")
            return

        # Add unique_id to each dictionary
        for entry in data:
            if "task_id" in entry and "model" in entry:
                entry["unique_id"] = f"{entry['task_id']}_{entry['model']}"
            else:
                print("Error: Missing 'task_id' or 'model' in one of the entries.")

        # Write the updated JSON list to the output file
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"Updated JSON list written to {output_file}")

    except FileNotFoundError:
        print(f"Error: File {json_file} not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON file format.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_json_file> <output_json_file>")
    else:
        input_json = sys.argv[1]
        output_json = sys.argv[2]
        add_unique_ids_to_json_list(input_json, output_json)
