import json
import csv
import sys
import os
import shutil
import pandas as pd
from collections import defaultdict

def load_json(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_csv(csv_path):
    return pd.read_csv(csv_path, dtype=str)

def find_matching_rows(df, unique_ids):
    return df[df["unique_id"].isin(unique_ids)]

def copy_matching_folders(source_folder, destination_folder, unique_ids):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    copied_folders = defaultdict(int)
    
    for root, dirs, _ in os.walk(source_folder):
        for folder in dirs:
            if folder in unique_ids:
                copied_folders[folder] += 1
                source_path = os.path.join(root, folder)
                destination_path = os.path.join(destination_folder, f"{folder}_{copied_folders[folder]}")
                
                if not os.path.exists(destination_path):
                    shutil.copytree(source_path, destination_path)

    print(f"Copied {sum(copied_folders.values())} folders to {destination_folder}")

def save_filtered_csv(df, destination_folder):
    total_csv_path = os.path.join(destination_folder, "total_shallow.csv")
    df.to_csv(total_csv_path, index=False)
    print(f"Filtered CSV saved to {total_csv_path}")

def main():
    if len(sys.argv) != 5:
        print("Usage: python script.py <json_dataset_path> <source_folder> <destination_folder> <csv_results_path>")
        sys.exit(1)

    json_path = sys.argv[1]
    source_folder = sys.argv[2]
    destination_folder = sys.argv[3]
    csv_path = sys.argv[4]

    json_data = load_json(json_path)
    df = load_csv(csv_path)

    unique_ids = {item["unique_id"] for item in json_data}

    filtered_df = find_matching_rows(df, unique_ids)
    copy_matching_folders(source_folder, destination_folder, unique_ids)
    save_filtered_csv(filtered_df, destination_folder)

if __name__ == "__main__":
    main()
