import json
import random
import os


def read_json(file_path):
    """
    Reads a JSON file and returns a list of data.
    """
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Unable to read the file '{file_path}': {e}")
        return []


def select_entries(ac_data, wa_data, num_true=100, num_false=100):
    """
    Randomly selects the specified number of true and false entries, ensuring all selected entries have unique task IDs.

    Parameters:
        ac_data (list): List of entries from `ac_data.json`.
        wa_data (list): List of entries from `wa_data.json`.
        num_true (int): Number of `correct: true` entries to select.
        num_false (int): Number of `correct: false` entries to select.

    Returns:
        selected_true (list): List of selected `correct: true` entries.
        selected_false (list): List of selected `correct: false` entries.
    """
    # Shuffle the lists
    random.shuffle(ac_data)
    random.shuffle(wa_data)

    selected_true = []
    selected_false = []
    used_task_ids = set()

    # Select `correct: true` entries
    for entry in ac_data:
        if len(selected_true) >= num_true:
            break
        task_id = entry["task_id"]
        if task_id not in used_task_ids:
            selected_true.append(entry)
            used_task_ids.add(task_id)

    # Select `correct: false` entries, avoiding duplicate task IDs
    for entry in wa_data:
        if len(selected_false) >= num_false:
            break
        task_id = entry["task_id"]
        if task_id not in used_task_ids:
            selected_false.append(entry)
            used_task_ids.add(task_id)

    # Check if the required number of entries is met
    if len(selected_true) < num_true:
        print(f"Warning: The number of available `correct: true` entries ({len(selected_true)}) is less than the requested {num_true}.")
    if len(selected_false) < num_false:
        print(f"Warning: The number of available `correct: false` entries ({len(selected_false)}) is less than the requested {num_false}.")

    return selected_true, selected_false


def split_into_files(selected_true, selected_false, num_files=20, true_per_file=5, false_per_file=5,
                     output_prefix="part"):
    """
    Splits the selected entries into multiple JSON files, each containing the specified number of true and false entries.

    Parameters:
        selected_true (list): List of selected `correct: true` entries.
        selected_false (list): List of selected `correct: false` entries.
        num_files (int): Number of JSON files to generate.
        true_per_file (int): Number of `correct: true` entries per file.
        false_per_file (int): Number of `correct: false` entries per file.
        output_prefix (str): Prefix for the output file names.
    """
    # Check if there are enough entries
    if len(selected_true) < num_files * true_per_file:
        print(f"Warning: The number of available `correct: true` entries ({len(selected_true)}) is less than the required {num_files * true_per_file}.")
    if len(selected_false) < num_files * false_per_file:
        print(f"Warning: The number of available `correct: false` entries ({len(selected_false)}) is less than the required {num_files * false_per_file}.")

    # Calculate the actual number of files that can be generated
    possible_files_true = len(selected_true) // true_per_file
    possible_files_false = len(selected_false) // false_per_file
    actual_num_files = min(num_files, possible_files_true, possible_files_false)

    if actual_num_files < num_files:
        print(f"Warning: Only {actual_num_files} files can be generated instead of the requested {num_files}.")

    # Shuffle the lists for randomness
    random.shuffle(selected_true)
    random.shuffle(selected_false)

    for i in range(actual_num_files):
        file_true = selected_true[i * true_per_file: (i + 1) * true_per_file]
        file_false = selected_false[i * false_per_file: (i + 1) * false_per_file]

        file_entries = file_true + file_false
        random.shuffle(file_entries)

        output_file = f"{output_prefix}_{i + 1}.json"
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(file_entries, f, indent=4, ensure_ascii=False)
            print(f"Generated '{output_file}' containing {len(file_true)} `true` and {len(file_false)} `false` entries.")
        except Exception as e:
            print(f"Unable to write the file '{output_file}': {e}")


def main():
    # Set the input JSON file paths
    ac_input_file = "ac_data.json"
    wa_input_file = "wa_data.json"

    # Read the JSON data
    ac_data = read_json(ac_input_file)
    wa_data = read_json(wa_input_file)

    if not ac_data and not wa_data:
        print("Error: No input data could be read.")
        return

    # Select 100 `correct: true` and 100 `correct: false` entries, ensuring unique task IDs
    selected_true, selected_false = select_entries(ac_data, wa_data, num_true=100, num_false=100)

    # Check if there are enough entries
    total_selected = len(selected_true) + len(selected_false)
    if total_selected < 200:
        print(f"Warning: The total number of selected entries ({total_selected}) is less than 200. Please check the input data.")

    # Split and save to 20 JSON files, each containing 10 entries (5 `true` and 5 `false`)
    split_into_files(
        selected_true,
        selected_false,
        num_files=20,
        true_per_file=5,
        false_per_file=5,
        output_prefix="part"
    )

    print("All files have been successfully generated.")


if __name__ == "__main__":
    main()
