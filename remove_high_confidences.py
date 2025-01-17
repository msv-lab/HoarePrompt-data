import json
import sys

# Define the script
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <group_consistencies.json> <tasks.json> <output.json>")
        sys.exit(1)

    # File paths from arguments
    group_consistencies_file = sys.argv[1]
    tasks_file = sys.argv[2]
    output_file = sys.argv[3]

    # Load the JSON data
    with open(group_consistencies_file, 'r') as f:
        group_consistencies = json.load(f)

    with open(tasks_file, 'r') as f:
        tasks = json.load(f)

    # Step 1: Find all task IDs with consistency != 1.0
    non_confident_ids = [
        item["unique_id"].replace("_human", "")
        for item in group_consistencies["group_consistencies"]
        if item["consistency"] < 0.98
    ]
    print(non_confident_ids)
    # Step 2: Select all entries from the second JSON where unique_id matches
    selected_tasks = [task for task in tasks if str(task["unique_id"]) in non_confident_ids]

    # Save the result to the output JSON file
    with open(output_file, "w") as f:
        json.dump(selected_tasks, f, indent=4)

    print(f"Filtered tasks saved to {output_file}")
