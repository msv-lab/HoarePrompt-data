import os
import json

def process_files(base_dir, output_ac_file, output_wa_file):
    """
    Reads the directory structure, processes files, and generates two JSON files.
    One for "ac" files and the other for "wa" files.
    """
    # Initialize lists to store AC and WA data
    ac_data = []
    wa_data = []

    # Initialize task counter
    task_id_counter = 0

    # Check if base_dir exists
    if not os.path.exists(base_dir):
        print(f"Error: The specified root directory '{base_dir}' does not exist. Please check the path.")
        return

    # Traverse all subfolders under the root directory
    for folder_name in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder_name)
        if os.path.isdir(folder_path) and folder_name.isdigit():
            # Process each folder named with numbers
            for file_name in os.listdir(folder_path):
                if file_name.endswith(".md") and file_name[:-3].isupper():
                    md_file_path = os.path.join(folder_path, file_name)
                    # Read the description
                    try:
                        with open(md_file_path, "r", encoding="utf-8") as md_file:
                            description = md_file.read().strip()
                    except Exception as e:
                        print(f"Unable to read file '{md_file_path}': {e}")
                        continue

                    # Extract the base name (e.g., extract "A" from "A.md")
                    base_name = file_name[:-3]

                    # Find corresponding .py files (there may be one or two)
                    py_files = [
                        f for f in os.listdir(folder_path)
                        if f.startswith(base_name) and f.endswith(".py")
                    ]

                    if not py_files:
                        print(f"Warning: No .py files found in folder '{folder_path}' corresponding to '{base_name}.md'.")
                        continue

                    task_id_counter += 1

                    for py_file in py_files:
                        py_file_path = os.path.join(folder_path, py_file)
                        # Read the Python code
                        try:
                            with open(py_file_path, "r", encoding="utf-8") as py_file_obj:
                                generated_code = py_file_obj.read().strip()
                        except Exception as e:
                            print(f"Unable to read file '{py_file_path}': {e}")
                            continue

                        # Determine whether the file is AC or WA
                        is_ac = "ac" in py_file.lower()
                        correct = is_ac

                        # Create a data dictionary
                        data_entry = {
                            "description": description,
                            "task_name": f"{folder_name}-{base_name}",
                            "dataset": "codeforces2024",
                            "model": "human",
                            "generated_code": generated_code,
                            "correct": correct,
                            "task_id": task_id_counter,
                        }

                        # Add data to the corresponding list
                        if is_ac:
                            ac_data.append(data_entry)
                        else:
                            wa_data.append(data_entry)

    # Write data to JSON files
    try:
        with open(output_ac_file, "w", encoding="utf-8") as ac_file:
            json.dump(ac_data, ac_file, indent=4, ensure_ascii=False)
        print(f"AC data saved to '{output_ac_file}'")
    except Exception as e:
        print(f"Unable to write file '{output_ac_file}': {e}")

    try:
        with open(output_wa_file, "w", encoding="utf-8") as wa_file:
            json.dump(wa_data, wa_file, indent=4, ensure_ascii=False)
        print(f"WA data saved to '{output_wa_file}'")
    except Exception as e:
        print(f"Unable to write file '{output_wa_file}': {e}")

if __name__ == "__main__":
    # Set the root directory path; modify as needed
    base_dir = "./newdata"  # Example: "/path/to/your/input_data"

    # Set the output JSON filenames
    output_ac_file = "ac_data.json"
    output_wa_file = "wa_data.json"

    # Call the function to process files
    process_files(base_dir, output_ac_file, output_wa_file)
