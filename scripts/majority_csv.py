import os
import pandas as pd
from collections import Counter

def find_and_process_csvs(directory, output_file):
    """
    Find all CSVs in a directory, concatenate them into a single DataFrame, 
    and process groups based on majority values for specified columns.

    Parameters:
    directory (str): Directory to search for CSV files.
    output_file (str): Path to save the processed CSV.
    """
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

            # columns_to_preprocess = ["original correctness", "summary fsl", "naive correctness fsl", "vanilla", "simple tree", "complex tree",  "summary" , "simple verify fsl", "complex verify fsl", "summary verify fsl", "simple verify", "complex verify", "summary verify"]

        # Columns to compute majority values for
        majority_columns = ["original correctness", "summary fsl", "naive correctness fsl", "vanilla", "simple tree", "complex tree",  "summary" , "simple verify fsl", "complex verify fsl", "summary verify fsl", "simple verify", "complex verify", "summary verify"]

        # Group by Task ID and model_created
        grouped = combined_df.groupby(["Task ID", "model_created"])

        # Process each group to find majority values
        majority_rows = []
        for (task_id, model), group in grouped:
            row = {
                "Task ID": task_id,
                "model_created": model
            }
            for column in majority_columns:
                # Find the most common value in the column for the group
                if column in group:
                    most_common_value = group[column].mode()[0] if not group[column].isnull().all() else None
                    row[column] = most_common_value
            majority_rows.append(row)

        # Create a new DataFrame with majority values
        majority_df = pd.DataFrame(majority_rows)

        # Save the resulting DataFrame to a new CSV
        majority_df.to_csv(output_file, index=False)
        print(f"Processed CSV written to {output_file}")
    else:
        print("No CSV files found.")

# Directory to search for CSV files
input_directory = "/home/jim/HoarePrompt-data/Results/Pilot_new1/apps_3point5"  # Replace with your directory path
output_csv = "/home/jim/HoarePrompt-data/Results/Pilot_new1/apps_3point5/majority_confidence_apps_3point5.csv"  # Replace with your desired output file name

# Call the function
find_and_process_csvs(input_directory, output_csv)
