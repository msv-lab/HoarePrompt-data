import json
import random
import re
from pathlib import Path


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_model_from_filename(file_name):
    if "gpt-4o" in file_name:
        return "gpt-4o"
    elif "llama3-70b" in file_name:
        return "llama3-70b"
    return "unknown"


def count_function_defs(code: str) -> int:
    pattern = r'\bdef\s+\w+\s*\('
    matches = re.findall(pattern, code)
    return len(matches)


def select_matched_tasks(data1, data2, model1, model2, dataset, sample_size=25):
    data2_dict = {task['task_id']: task for task in data2}

    matched_tasks = []
    random.shuffle(data1)

    for task in data1:
        task_id = task['task_id']

        if task_id in data2_dict:
            code1 = task.get('generated_code')
            code2 = data2_dict[task_id].get('generated_code')

            if count_function_defs(code1) <= 1 and count_function_defs(code2) <= 1:
                matched_task = [
                    {
                        "task_id": task_id,
                        "dataset": dataset,
                        "model": model1,
                        **task
                    },
                    {
                        "task_id": task_id,
                        "dataset": dataset,
                        "model": model2,
                        **data2_dict[task_id]
                    }
                ]
                matched_tasks.append(matched_task)

        if len(matched_tasks) == sample_size:
            break

    return matched_tasks


if __name__ == "__main__":
    data_folder = Path("data")

    # data file path
    apps_llama_file = data_folder / "apps_llama3-70b-8192_20240906.json"
    apps_gpt_file = data_folder / "apps_gpt-4o-2024-05-13_20240906.json"
    mbpp_llama_file = data_folder / "mbppplus_llama3-70b-8192_20240908.json"
    mbpp_gpt_file = data_folder / "mbppplus_gpt-4o-2024-05-13_20240908.json"

    apps_llama_data = load_data(apps_llama_file)
    apps_gpt_data = load_data(apps_gpt_file)
    mbpp_llama_data = load_data(mbpp_llama_file)
    mbpp_gpt_data = load_data(mbpp_gpt_file)

    # get model name
    apps_llama_name = get_model_from_filename(apps_llama_file.name)
    apps_gpt_name = get_model_from_filename(apps_gpt_file.name)
    apps_dataset = "apps"

    mbpp_llama_name = get_model_from_filename(mbpp_llama_file.name)
    mbpp_gpt_name = get_model_from_filename(mbpp_gpt_file.name)
    mbpp_dataset = "mbpp"

    matched_apps_tasks = select_matched_tasks(apps_llama_data, apps_gpt_data, apps_llama_name, apps_gpt_name, apps_dataset)
    matched_mbpp_tasks = select_matched_tasks(mbpp_llama_data, mbpp_gpt_data, mbpp_llama_name, mbpp_gpt_name, mbpp_dataset)

    combined_data = matched_apps_tasks + matched_mbpp_tasks

    output_file = data_folder / "pilot.json"
    save_to_json(combined_data, output_file)

    print(f"Selected {len(matched_apps_tasks)} matched tasks from APPs and {len(matched_mbpp_tasks)} matched tasks from MBPP.")
    print(f"Results saved to {output_file}")
