import json
from collections import defaultdict


def categorize_by_comment(input_file):
    # Load the JSON data from the provided file
    with open(input_file, 'r') as f:
        json_data = json.load(f)

    categorized_data = defaultdict(list)  # Using defaultdict to store lists of categorized items

    # Iterate through the list of dictionaries and categorize based on the 'comment' field
    for item in json_data:
        comment = item.get('comment', 'no_comment')  # Default to 'no_comment' if comment is missing
        categorized_data[comment].append(item)

    # Write categorized data into separate files
    for comment, items in categorized_data.items():
        # Prepare filename by sanitizing comment (to avoid invalid characters)
        filename = f"{comment.replace(' ', '_').replace('/', '_')}.json"

        # Save the categorized data into a file
        with open(filename, 'w') as f:
            json.dump(items, f, indent=4)

    print(f"Data categorized and saved in {len(categorized_data)} files.")


# Call the function with the JSON input file
input_file = 'manual_again.json'  # Change this to the path of your input JSON file
categorize_by_comment(input_file)