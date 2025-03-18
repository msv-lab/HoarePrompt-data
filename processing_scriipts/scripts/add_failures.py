import os
import sys
import json
import pandas as pd


def process_results(json_path, csv_path):
    # Load the JSON dataset
    with open(json_path, "r", encoding="utf-8") as f:
        dataset = json.load(f)
    
    # Extract unique IDs from dataset
    unique_ids = {entry["unique_id"]: entry["correct"] for entry in dataset}
    
    # Load the CSV file
    df = pd.read_csv(csv_path)
    
    # Count occurrences of each unique_id in the CSV
    counts = df["unique_id"].value_counts()
    
    # Prepare missing entries
    missing_rows = []
    for unique_id, original_correctness in unique_ids.items():
        missing_count = 3 - counts.get(unique_id, 0)
        if missing_count > 0:
            for _ in range(missing_count):
                missing_rows.append({
                    "Task ID": "",  # Leave empty or extract from dataset if needed
                    "unique_id": unique_id,
                    "Dataset": "",  # Leave empty or extract from dataset if needed
                    "model_created": "",  # Leave empty
                    "model_run": "",  # Leave empty
                    "description": "",  # Leave empty or extract from dataset if needed
                    "Code": "",  # Leave empty
                    "run_number": "",  # Leave empty
                    "original correctness": original_correctness,
                    "vanilla": not original_correctness  # Opposite of original_correctness
                })
    
    # Append missing rows to dataframe
    if missing_rows:
        df = pd.concat([df, pd.DataFrame(missing_rows)], ignore_index=True)
    
    # Save updated results
    output_path = os.path.join(os.path.dirname(csv_path), "total_plus.csv")
    df.to_csv(output_path, index=False)
    print(f"Updated results saved to {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <path_to_json> <path_to_csv>")
        sys.exit(1)
    
    json_path = sys.argv[1]
    csv_path = sys.argv[2]
    process_results(json_path, csv_path)
