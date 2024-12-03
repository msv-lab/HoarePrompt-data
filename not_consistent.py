import pandas as pd
import json
import sys
import os

# Load input arguments
json_file = sys.argv[1]
csv_file = sys.argv[2]

# Load JSON file
with open(json_file, 'r') as f:
    group_consistencies = json.load(f)

# Convert JSON to DataFrame
json_df = pd.DataFrame(group_consistencies["group_consistencies"])

# Load CSV file
csv_data = pd.read_csv(csv_file)

# Create unique_id and map consistency
def generate_unique_id(row):
    task_id = str(row["Task ID"]).zfill(4)
    return f"{task_id}_{row['model_created']}"

csv_data['unique_id'] = csv_data.apply(generate_unique_id, axis=1)
csv_data = csv_data.merge(json_df, on="unique_id", how="left")

# Save augmented CSV
output_folder = os.path.dirname(csv_file)
augmented_csv_path = os.path.join(output_folder, "augmented.csv")
csv_data.to_csv(augmented_csv_path, index=False)

# Filter rows based on consistency
csv_1 = csv_data[csv_data['consistency'] != 1.0]
csv_2 = csv_data[~csv_data['consistency'].isin([1.0, 0.9])]
csv_3 = csv_data[~csv_data['consistency'].isin([1.0, 0.9, 0.8])]
csv_4 = csv_data[~csv_data['consistency'].isin([1.0, 0.9, 0.8, 0.7])]

# Save filtered CSVs
csv_1.to_csv(os.path.join(output_folder, "filtered_consistency_1.csv"), index=False)
csv_2.to_csv(os.path.join(output_folder, "filtered_consistency_1_09.csv"), index=False)
csv_3.to_csv(os.path.join(output_folder, "filtered_consistency_1_09_08.csv"), index=False)
csv_4.to_csv(os.path.join(output_folder, "filtered_consistency_1_09_08_07.csv"), index=False)