import json

def convert_data(input_json):
    new_data = []
    task_id_counter = 1  # 初始化 task_id 为 1

    for item in input_json:
        new_item = {
            "description": item["question"],
            "task_name": item["task_id"],
            "dataset": "apps",  # 可以修改
            "model": "llama3-70b",            # 可以修改
            "generated_code": item["generated_code"],
            "correct": (item["pass_rate"] == 1.0),
            "task_id": str(task_id_counter)
        }
        new_data.append(new_item)
        task_id_counter += 1  # 递增 task_id

    return new_data

def process_json(input_filename, output_filename):
    with open(input_filename, 'r') as f:
        input_data = json.load(f)

    output_data = convert_data(input_data)

    with open(output_filename, 'w') as f:
        json.dump(output_data, f, indent=4)

# 使用脚本处理 JSON 文件
input_filename = 'apps_llama3-70b-final.json'  # 输入文件名
output_filename = 'apps_llama3-70b_final_stdformat.json'  # 输出文件名
process_json(input_filename, output_filename)