import re
import argparse
import json
import ast
from pathlib import Path
from datetime import datetime

from model import get_model, Model
from mbppplus_test import execute_tests, summary

CODE_GEN_PROMPT = """
You are an expert Python programmer. Your task is to provide code according to the specification. Your code should pass the provided tests. Ensure that the function name is consistent.


Example1: 
You are an expert Python programmer, and here is your task: Write a function to find the shared elements from the given two lists. Your code should pass these tests:\n\n\nassert similar_elements((3, 4, 5, 6),(5, 7, 4, 10)) == (4, 5)\nassert similar_elements((1, 2, 3, 4),(5, 4, 3, 7)) == (3, 4)\nassert similar_elements((11, 12, 14, 13),(17, 15, 14, 13)) == (13, 14)\n


Example Answer: \n```\ndef similar_elements(test_tup1, test_tup2):\n  return tuple(set(test_tup1) & set(test_tup2))\n```\n


Example2:
You are an expert Python programmer, and here is your task: Write a python function to identify non-prime numbers. Your code should pass these tests:\n\n\nassert is_not_prime(1) == True\nassert is_not_prime(2) == False\nassert is_not_prime(10) == True\nassert is_not_prime(35) == True\nassert is_not_prime(37) == False\n


Example Answer: \n```\nimport math\ndef is_not_prime(n):\n    if n == 1:\n        return True\n    for i in range(2, int(math.sqrt(n))+1):\n        if n % i == 0:\n            return True\n    return False\n```\n


Example3:
You are an expert Python programmer, and here is your task: Write a function to find the n largest integers from a given list of numbers, returned in descending order. Your code should pass these tests:\n\n\nassert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]\nassert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],2)==[85, 75]\nassert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],5)==[85, 75, 65, 58, 35]\n


Example Answer: \n```\nimport heapq as hq\ndef heap_queue_largest(nums: list,n: int) -> list:\n  largest_nums = hq.nlargest(n, nums)\n  return largest_nums\n```\n


Your Task:
You are an expert Python programmer, and here is your task: {prompt},  Your code should pass these tests:\n\n{test}
"""


def clean_prompt(prompt: str) -> str:
    cleaned_prompt = re.sub(r"assert\s+.*", "", prompt).strip()
    cleaned_prompt = cleaned_prompt.strip('\"').strip()
    return cleaned_prompt


def get_code(data, model, output_file: Path):
    output_file.parent.mkdir(parents=True, exist_ok=True)

    results = []

    for task in data:
        task_id = task['task_id']
        prompt = task['prompt']
        test = task["assertion"]

        specification = clean_prompt(prompt)
        formatted_prompt = CODE_GEN_PROMPT.format(prompt=prompt, test=test)

        max_attempts = 3
        attempts = 0
        success = False
        generated_code = ""

        while attempts < max_attempts and not success:
            attempts += 1
            response = model.query(formatted_prompt)
            generated_code = extract_code_from_response(response)

            try:
                ast.parse(generated_code)
                success = True
            except SyntaxError:
                print(f"Task {task_id}: Syntax error on attempt {attempts}. Retrying...")

        if success:
            total_tests, passed_tests, test_results = execute_tests(task, generated_code)

            pass_rate = summary(passed_tests, total_tests)
            result = {
                'task_id': task_id,
                'specification': specification,
                'generated_code': generated_code,
                'pass_rate': pass_rate,
                'test_results': test_results
            }

            print("*" * 50)
            print(f"finish task: {task_id}")
            results.append(result)
        else:
            print(f"Task {task_id}: Failed to generate valid code after {max_attempts} attempts. Skipping...")

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print(f"Results saved to {output_file}")


def extract_code_from_response(response_content: str) -> str:
    code_pattern = r"```(?:python)?\n(.*?)```"
    match = re.search(code_pattern, response_content, re.DOTALL)
    if match:
        return match.group(1)
    return response_content


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="mbppplus code generation")
    parser.add_argument('--save', type=str, help="Directory to save result")

    args = parser.parse_args()

    if args.save:
        output_dir = Path(args.save)
    else:
        output_dir = Path('data')

    with open("MbppPlus.jsonl", "r") as f:
        mbpp_data = [json.loads(line) for line in f]

    # model_name = "gpt-4o-2024-05-13"
    model_name = "llama3-70b-8192"
    model = get_model(model_name, 0.7)

    timestamp = datetime.now().strftime("%Y%m%d")
    output_file = output_dir / f"mbppplus_{model_name}_{timestamp}.json"

    get_code(mbpp_data, model, output_file)
