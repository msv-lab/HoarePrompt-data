import json
import csv
import sys
import os
from collections import Counter

def load_json(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_csv(csv_path):
    unique_ids = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if "unique_id" in row:
                unique_ids.append(row["unique_id"])
    return unique_ids

def find_missing_items(json_data, csv_unique_ids, required_count=3):
    id_counter = Counter(csv_unique_ids)
    missing_items = []
    
    for item in json_data:
        unique_id = item["unique_id"]
        missing_count = required_count - id_counter.get(unique_id, 0)
        if missing_count > 0:
            missing_items.extend([item] * missing_count)
    
    return missing_items

def save_missing_json(json_path, missing_items):
    rerun_json_path = os.path.join(os.path.dirname(json_path), "reruns1.json")
    with open(rerun_json_path, "w", encoding="utf-8") as f:
        json.dump(missing_items, f, indent=4)
    print(f"Missing items JSON saved to: {rerun_json_path}")

def filter_rerun_json(rerun_json_path, csv_path):
    rerun_data = load_json(rerun_json_path)
    csv_results = {}
    
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            unique_id = row["unique_id"]
            correctness = row["original_correctness"]
            if unique_id not in csv_results:
                csv_results[unique_id] = []
            csv_results[unique_id].append(correctness)
    
    updated_rerun_data = []
    removed_ids = []
    
    id_counts = Counter([item["unique_id"] for item in rerun_data])
    removed_count = Counter()
    
    for item in rerun_data:
        unique_id = item["unique_id"]
        if unique_id in csv_results and "vanilla" not in csv_results[unique_id]:
            if removed_count[unique_id] < id_counts[unique_id]:
                removed_count[unique_id] += 1
                removed_ids.append(unique_id)
                continue
        updated_rerun_data.append(item)
    
    with open(rerun_json_path, "w", encoding="utf-8") as f:
        json.dump(updated_rerun_data, f, indent=4)
    
    print("Removed unique IDs:")
    print("\n".join(set(removed_ids)))

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <json_dataset_path> <csv_results_path> [<csv_filter_path>]")
        sys.exit(1)
    
    json_path = sys.argv[1]
    csv_path = sys.argv[2]
    
    json_data = load_json(json_path)
    csv_unique_ids = load_csv(csv_path)
    missing_items = find_missing_items(json_data, csv_unique_ids)
    save_missing_json(json_path, missing_items)
    
    if len(sys.argv) == 4:
        rerun_json_path = os.path.join(os.path.dirname(json_path), "reruns1.json")
        filter_rerun_json(rerun_json_path, sys.argv[3])

if __name__ == "__main__":
    main()