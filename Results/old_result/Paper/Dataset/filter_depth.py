import json
import sys
import os

def load_json(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def split_by_depth(json_data):
    shallow = [item for item in json_data if item.get("depth") in [0, 1]]
    deep = [item for item in json_data if item.get("depth") == 2]
    return shallow, deep

def save_json(json_path, data, filename):
    save_path = os.path.join(os.path.dirname(json_path), filename)
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"Saved {filename} with {len(data)} entries.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <json_dataset_path>")
        sys.exit(1)

    json_path = sys.argv[1]
    json_data = load_json(json_path)
    
    shallow_data, deep_data = split_by_depth(json_data)
    
    save_json(json_path, shallow_data, "paper_shallow.json")
    save_json(json_path, deep_data, "paper_deep.json")

if __name__ == "__main__":
    main()
