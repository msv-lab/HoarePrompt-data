import json
import random
from pathlib import Path

def load_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def save_data(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def select_random_tasks(data1, data2, num_pairs):
    # Ensure data1 and data2 are aligned by task_id
    data1_dict = {item['task_id']: item for item in data1 if item['depth']< 3}
    data2_dict = {item['task_id']: item for item in data2 if item['depth']< 3}


    # Get common task_ids
    common_task_ids = list(set(data1_dict.keys()) & set(data2_dict.keys()))

    # Randomly sample task_ids
    selected_task_ids = random.sample(common_task_ids, min(num_pairs, len(common_task_ids)))

    # Extract the paired items
    selected_data =[]
    for task_id in selected_task_ids:
        selected_data.append(data1_dict[task_id])
        selected_data.append(data2_dict[task_id])
    

    return selected_data

# Hardcoded file paths
data_folder = Path("/home/jim/HoarePrompt-data/PilotData/data")
apps_llama_file = data_folder / "mbppplus_llama3point1-70b_final_stdformat_depth.json"
apps_gpt_file = data_folder / "mbppplus_gpt-4o_final_stdformat_depth.json"

# Load the data
apps_llama_data = load_data(apps_llama_file)
apps_gpt_data = load_data(apps_gpt_file)

# Select 75 task pairs
num_pairs = 75
selected_tasks = select_random_tasks(apps_llama_data, apps_gpt_data, num_pairs)

# Save the selected tasks to a single JSON file
output_file = data_folder / "selected_pilot_75_tasks.json"
save_data(selected_tasks, output_file)

print(f"Selected tasks saved to {output_file}")
