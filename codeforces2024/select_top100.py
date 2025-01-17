import json


def sort_and_select_top(input_file, output_file, top_n=100):
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
        # Sort sublists by the number of dictionaries in descending order
        sorted_data = sorted(data, key=lambda sublist: sum(1 for item in sublist if isinstance(item, dict)),
                             reverse=True)

        # Select the top `top_n` sublists
        top_data = sorted_data[:top_n]

        # Print the number of dictionaries in each selected sublist
        print(f"Top {top_n} sublists with dictionary counts:")
        for idx, sublist in enumerate(top_data, 1):
            dict_count = sum(1 for item in sublist if isinstance(item, dict))
            print(f"Sublist {idx}: {dict_count} dictionaries")

        # Write the selected sublists to the output JSON file
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(top_data, file, ensure_ascii=False, indent=4)

        print(f"Top {top_n} sublists have been saved to {output_file}.")
    except Exception as e:
        print(f"Error during data processing: {e}")
        return


# Example usage
input_file = 'codeforces2024_172.json'  # Path to the input JSON file
output_file = 'codeforces2024_top100.json'  # Path to the output JSON file
sort_and_select_top(input_file, output_file)