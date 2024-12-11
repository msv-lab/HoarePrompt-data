import json
import random
import re
from pathlib import Path
import argparse

# Load JSON data from a specified file path
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Save data to a JSON file
def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# This function serves to extract the high level model name from the file name
def get_model_from_filename(file_name):
   #split after the first underscore and remove the extension
    return file_name.split("_")[1].split(".")[0]

# Count the number of function definitions in a given code string using regex
def count_function_defs(code: str) -> int:
    pattern = r'\bdef\s+\w+\s*\('
    matches = re.findall(pattern, code)
    return len(matches)

# Determine if the task is correct based on pass rates or accuracies for the given dataset
# For apps pass rate must be 1, for mbpp base_accuracy and plus_accuracy must be 1 and assertion_passed must be True
def is_task_correct(task, dataset):
    if dataset == "apps":
        return task.get("pass_rate") == 1
    elif dataset == "mbpp":
        return (
            task.get("base_accuracy") == 1
            and task.get("plus_accuracy") == 1
            and task.get("assertion_passed") is True
        )
    return False

# Select matched tasks between two datasets and shuffle them randomly for a given sample size
def select_matched_tasks(data1, data2, model1, model2, dataset, sample_size=25):
    data2_dict = {task['task_id']: task for task in data2}

    matched_tasks = []
    random.shuffle(data1)

    for task in data1:
        task_id = task['task_id']

        # find same task in data2
        if task_id in data2_dict:
            task1_correct = is_task_correct(task, dataset)
            task2_correct = is_task_correct(data2_dict[task_id], dataset)
            task1_ce = task.get("counterexample")
            task2_ce = data2_dict[task_id].get("counterexample")

            matched_tasks.append({
                "task_id": task_id,
                "dataset": dataset,
                "model": model1,
                "correct": task1_correct,
                "description": task['description'],
                "generated_code": task["generated_code"],
                "counter_example": task1_ce
            })
            matched_tasks.append({
                "task_id": task_id,
                "dataset": dataset,
                "model": model2,
                "correct": task2_correct,
                "description": data2_dict[task_id].get("specification") or data2_dict[task_id].get("question"),
                "generated_code": data2_dict[task_id]["generated_code"],
                "counter_example": task2_ce
            })

        # count the example
        if len(matched_tasks) // 2 == sample_size:
            break

    return matched_tasks


if __name__ == "__main__":
    data_folder = Path("data")

    # get as argument the sample size 
    # if not provided use 25 as default
    parser = argparse.ArgumentParser(description='Process sample size.')
    parser.add_argument('--sample_size', type=int, default=25, help='Size of the sample (default: 25)')
    args = parser.parse_args()
    
    sample_size = args.sample_size
    print(f'Sample size: {sample_size}')


    # data file path they are hardcoded to the once we have generated in the past
    apps_llama_file = data_folder / "apps_llama3-70b_final_stdformat.json"
    apps_gpt_file = data_folder / "apps_gpt-4o_final_stdformat.json"
    mbpp_llama_file = data_folder / "mbppplus_llama3point1-70b_final_stdformat.json"
    mbpp_gpt_file = data_folder / "mbppplus_gpt-4o_final_stdformat.json"
    
    # Load the data from the files
    apps_llama_data = load_data(apps_llama_file)
    apps_gpt_data = load_data(apps_gpt_file)
    mbpp_llama_data = load_data(mbpp_llama_file)
    mbpp_gpt_data = load_data(mbpp_gpt_file)

    # get model name without date and extension
    apps_llama_name = get_model_from_filename(apps_llama_file.name)
    apps_gpt_name = get_model_from_filename(apps_gpt_file.name)
    apps_dataset = "apps"

    mbpp_llama_name = get_model_from_filename(mbpp_llama_file.name)
    mbpp_gpt_name = get_model_from_filename(mbpp_gpt_file.name)
    mbpp_dataset = "mbpp"

    matched_apps_tasks = select_matched_tasks(apps_llama_data, apps_gpt_data, apps_llama_name, apps_gpt_name, apps_dataset,sample_size)
    matched_mbpp_tasks = select_matched_tasks(mbpp_llama_data, mbpp_gpt_data, mbpp_llama_name, mbpp_gpt_name, mbpp_dataset,sample_size)

    combined_data = matched_apps_tasks + matched_mbpp_tasks

    #save they created sample to a file named pilot_num.json
    #check if there is pilot.json and increase a counter until it does not exist
    # counter = 1
    # while (data_folder / f"pilot{counter}.json").exists():
    #     counter += 1
    # output_file = data_folder / f"pilot{counter}_size_{sample_size}.json"
    output_file = data_folder / f"pilot_apps_final_size_{sample_size}.json"
    save_to_json(matched_apps_tasks, output_file)
    output_file = data_folder / f"pilot_mbpp_final_size_{sample_size}.json"
    save_to_json(matched_mbpp_tasks, output_file)

    print(f"Selected {len(matched_apps_tasks) // 2} matched tasks from APPs and {len(matched_mbpp_tasks) // 2} matched tasks from MBPP.")
    print(f"Results saved to {output_file}")
