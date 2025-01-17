import json
import random

def select_random_six_count(input_file, output_file, sample_size=100):
    try:
        # Read the JSON file
        with open(input_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError as e:
        print(f"Error: Input file not found. {e}")
        return
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON. {e}")
        return

    try:
        # Find all sublists with exactly 6 dictionaries
        six_count_sublists = [
            sublist for sublist in data
            if isinstance(sublist, list) and sum(1 for item in sublist if isinstance(item, dict)) == 6
        ]

        # Randomly select up to `sample_size` sublists
        selected_sublists = random.sample(six_count_sublists, min(sample_size, len(six_count_sublists)))

        print(len(selected_sublists))
        # Write the selected sublists to the output JSON file
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(selected_sublists, file, ensure_ascii=False, indent=4)

        print(f"Selected {len(selected_sublists)} sublists with exactly 6 dictionaries have been saved to {output_file}.")
    except Exception as e:
        print(f"Error during data processing: {e}")
        return


# Example usage
input_file = 'codeforces2024_172.json'  # Path to the input JSON file
output_file = 'codeforce2024_100wz6.json'  # Path to the output JSON file
select_random_six_count(input_file, output_file)