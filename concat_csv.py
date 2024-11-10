import os
import pandas as pd

def concat_csv_files(input_dir, output_file):
    # List to store dataframes
    csv_files = []
    
    # Iterate over all subdirectories one level deep
    for root, dirs, files in os.walk(input_dir):
        if root == input_dir:
            for dir in dirs:
                sub_dir = os.path.join(input_dir, dir)
                for file in os.listdir(sub_dir):
                    # Check for CSV files
                    if file.endswith('.csv'):
                        file_path = os.path.join(sub_dir, file)
                        # Read each CSV and append to list
                        csv_files.append(pd.read_csv(file_path))
            break  # Ensures only one level of subdirectories is traversed

    # Concatenate all dataframes
    if csv_files:
        combined_csv = pd.concat(csv_files, ignore_index=True)
        # Save to output file
        combined_csv.to_csv(output_file, index=False)
        print(f"All CSV files combined into {output_file}")
    else:
        print("No CSV files found in subdirectories")

# Usage
input_directory = '/home/jim/HoarePrompt-data/Results/Pilot_reruns/mbpp_4_mini_1'
output_csv = 'combined_output_mbpp_4mini_1csv'
concat_csv_files(input_directory, output_csv)
