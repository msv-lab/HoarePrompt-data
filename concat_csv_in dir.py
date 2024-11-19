import os
import pandas as pd

def find_and_concat_csvs(directory, output_file):
    # List to hold all dataframes
    all_dataframes = []

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                # Full path to the file
                file_path = os.path.join(root, file)
                try:
                    # Read CSV into a DataFrame and append to the list
                    df = pd.read_csv(file_path)
                    all_dataframes.append(df)
                    print(f"Loaded {file_path}")
                except Exception as e:
                    print(f"Failed to read {file_path}: {e}")

    # Concatenate all DataFrames if any are loaded
    if all_dataframes:
        combined_df = pd.concat(all_dataframes, ignore_index=True)
        combined_df.to_csv(output_file, index=False)
        print(f"Combined CSV written to {output_file}")
    else:
        print("No CSV files found.")

# Directory to search for CSV files
input_directory = "/home/jim/HoarePrompt-data/Results/Pilot_confidence_simple/apps_3point5_1"  # Replace with your directory path
output_csv = "/home/jim/HoarePrompt-data/Results/Pilot_confidence_simple/apps_3point5_1/combined_confidence_apps_3point5.csv"         # Replace with your desired output file name

# Call the function
find_and_concat_csvs(input_directory, output_csv)
