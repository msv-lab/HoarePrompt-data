import json
import random
from pathlib import Path


def load_random_samples(file_path, sample_size=25):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return random.sample(data, sample_size)


def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    data_folder = Path("data")
    apps_llama_file = data_folder / "apps_llama3-70b-8192_20240906.json"
    apps_gpt_file = data_folder / "apps_gpt-4o-2024-05-13_20240906.json"
    mbppplus_llama_file = data_folder / "mbppplus_llama3-70b-8192_20240906.json"
    mbppplus_gpt_file = data_folder / "mbppplus_llama3-70b-8192_20240906.json"

    combined_data = []
    combined_data.extend(load_random_samples(apps_llama_file))
    combined_data.extend(load_random_samples(apps_gpt_file))
    combined_data.extend(load_random_samples(mbppplus_llama_file))
    combined_data.extend(load_random_samples(mbppplus_gpt_file))

    output_file = data_folder / "pilot.json"
    save_to_json(combined_data, output_file)
