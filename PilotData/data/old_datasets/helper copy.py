import json

# Load the JSON datasets
with open('/home/jim/HoarePrompt-data/PilotData/data/pilot_mbpp_old.json', 'r') as file:
    first_dataset = json.load(file)

with open('/home/jim/HoarePrompt-data/PilotData/data/old_datasets/mbppplus_llama3point1-70b-final.json', 'r') as file:
    second_dataset = json.load(file)

with open('/home/jim/HoarePrompt-data/PilotData/data/old_datasets/mbppplus_gpt-4o-final.json', 'r') as file:
    third_dataset = json.load(file)

# Create a dictionary for quick lookup in the second dataset by task_name
second_dataset_lookup = {entry['task_id']: entry for entry in second_dataset}
third_dataset_lookup = {entry['task_id']: entry for entry in third_dataset}

# Process the first dataset
for entry in first_dataset:
    # Replace `depth` with `nested_loop_depth`
    if 'depth' in entry:
        entry['nested_loop_depth'] = entry.pop('depth')

    # Replace `task_id` with `task_name`
    if 'task_name' in entry:
        entry['task_id'] = entry['task_name'].replace("Mbpp/", "")
    # Find the corresponding entry in the second dataset and copy `counterexample`
    task_name = entry['task_name']
    if entry["model"]== "llama3-70b" or entry["model"]== "llama3point1-70b":
        if task_name in second_dataset_lookup:
            entry['counterexample'] = second_dataset_lookup[task_name].get('counterexample')
    elif entry["model"]== "gpt-4o":
        if task_name in third_dataset_lookup:
            entry['counterexample'] = third_dataset_lookup[task_name].get('counterexample')
    else:
        print("Model not found")
# Save the updated first dataset
with open('/home/jim/HoarePrompt-data/PilotData/data/pilot_mbpp.json', 'w') as file:
    json.dump(first_dataset, file, indent=4)

print("Updated first dataset saved to 'updated_first_dataset.json'")
