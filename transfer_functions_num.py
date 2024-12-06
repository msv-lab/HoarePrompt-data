import json
import csv
import sys

def process_csv_and_json(json_path, csv_path):
    try:
        # Load the JSON data
        with open(json_path, 'r', encoding='utf-8') as json_file:
            json_data = json.load(json_file)

        # Read the CSV data
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = list(csv.DictReader(csv_file))

        # Create a lookup dictionary for the JSON data based on task_id and model
        lookup = {}
        for item in json_data:
            key = (item['task_id'], item['model'])
            if key in lookup:
                print(f"Error: Duplicate entries found in JSON for task_id={item['task_id']} and model={item['model']}.")
                return
            lookup[key] = item['functions']

        # Add the 'functions' column to the CSV rows
        for row in reader:
            key = (row['Task ID'], row['model_created'])
            row['functions'] = lookup.get(key, None)  # Add 'None' if no match is found

        # Write the updated CSV
        output_csv_path = csv_path
        with open(output_csv_path, 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=list(reader[0].keys()))
            writer.writeheader()
            writer.writerows(reader)

        print(f"Processed CSV successfully written to {output_csv_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <path_to_json_file> <path_to_csv_file>")
    else:
        process_csv_and_json(sys.argv[1], sys.argv[2])