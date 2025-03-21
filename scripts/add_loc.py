import json
import sys
import os

def count_loc(code: str) -> int:
    """Counts non-empty lines in the provided code."""
    return sum(1 for line in code.splitlines() if line.strip())

def main(input_path: str, output_path: str):
    if not os.path.exists(input_path):
        print(f"Error: File {input_path} does not exist.")
        return

    # Load input JSON
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Add LOC field
    for item in data:
        code = item.get("generated_code", "")
        item["LOC"] = count_loc(code)

    # Save output JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"LOC added to {len(data)} items and saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python add_loc_to_json.py <input_path> <output_path>")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
        main(input_path, output_path)
