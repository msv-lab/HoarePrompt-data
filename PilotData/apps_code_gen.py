import re
import argparse
import json
from pathlib import Path
from datetime import datetime
from model import get_model, Model
from apps_test import execute_tests
from order_analysis import analyze_order_sensitivity, analyze_case_sensitivity

# The prompt that defines the basic structure used to instruct the LLM for code generation
SYSTEM_PROMPT = '''
You have been assigned the role of a Python program developer. You need to provide a program that meets the given requirements. There are two types of formats:

- If you see 'Use Standard Input format' at the end of the problem, you should directly read input using the `input()` function and provide executable code. The answer should be output using `print`, and no additional information beyond the answer should be printed.
- If you see 'Use Call-Based format,' you should provide the solution based on the provided program start, without modifying the program start.

Please follow the respective format based on the instructions given.


Example1:
QUESTION:
An accordion is a string (yes, in the real world accordions are musical instruments, but let's forget about it for a while) which can be represented as a concatenation of: an opening bracket (ASCII code $091$), a colon (ASCII code $058$), some (possibly zero) vertical line characters (ASCII code $124$), another colon, and a closing bracket (ASCII code $093$). The length of the accordion is the number of characters in it.

For example, [::], [:||:] and [:|||:] are accordions having length $4$, $6$ and $7$. (:|:), {:||:}, [:], ]:||:[ are not accordions. 

You are given a string $s$. You want to transform it into an accordion by removing some (possibly zero) characters from it. Note that you may not insert new characters or reorder existing ones. Is it possible to obtain an accordion by removing characters from $s$, and if so, what is the maximum possible length of the result?


-----Input-----

The only line contains one string $s$ ($1 \le |s| \le 500000$). It consists of lowercase Latin letters and characters [, ], : and |.


-----Output-----

If it is not possible to obtain an accordion by removing some characters from $s$, print $-1$. Otherwise print maximum possible length of the resulting accordion.


-----Examples-----
Input
|[a:b:|]

Output
4

Input
|]:[|:]

Output
-1
Use Standard Input format


Example Answer:
```
s = input()
n = len(s)
ind = -1
f = False
for i in range(n):
    if s[i] == '[':
        f = True
    elif s[i] == ':':
        if f:
            ind = i
            break
bind = -1
f = False
for i in range(n-1,-1,-1):
    if s[i] == ']':
        f = True
    elif s[i] == ':':
        if f:
            bind = i
            break
# print(ind,bind)
if ind == -1 or bind == -1:
    print(-1)
elif ind >= bind:
    print(-1)
else:
    ans = 4
    for i in range(ind+1,bind):
        if s[i] == '|':
            ans += 1
    print(ans)
```


Example2:
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:


Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:


Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

STARTER CODE:
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

Use Call-Based format


Example Answer:
```
class Solution:
     def searchRange(self, nums, target):
         """
         :type nums: List[int]
         :type target: int
         :rtype: List[int]
         """
         start = self.firstGreaterEqaul(nums, target)
         if start==len(nums) or nums[start]!=target:
             return [-1, -1]
         return [start, self.firstGreaterEqaul(nums, target+1)-1]
     def firstGreaterEqaul(self, nums, target):
         lo, hi = 0, len(nums)
         while lo<hi:
             mid = (hi+lo)//2
             if nums[mid]<target:
                 lo = mid + 1
             else:
                 hi = mid
         return lo
```


Your Task:
'''

# Function to generate the prompt sent to the LLM based on the prompt template from earlier
def generate_prompt(test_case, prompt, starter_code=None):
    _input = SYSTEM_PROMPT
    _input += "QUESTION:\n"
    data = prompt
    _input += data
    if starter_code != None:
        data = starter_code
        data = "\n\nSTARTER CODE:\n" + data
        _input += data
    else:
        pass

    data = test_case
    if not data.get("fn_name"):
        _input += "\nUse Standard Input format"
    else:
        _input += "\nUse Call-Based format"

    _input += "\nANSWER:\n"
    return _input

# Function to load problem data from a directory . It assumes a certain structure for the problem directory
def load_problem_data(problem_dir):
    problem = {}

    # Read question.txt
    question_file = problem_dir / 'question.txt'
    if question_file.exists():
        with open(question_file, 'r') as f:
            problem["question"] = f.read().strip()
    else:
        problem["question"] = None

    # Read input_output.json
    input_output_file = problem_dir / 'input_output.json'
    if input_output_file.exists():
        with open(input_output_file, 'r') as f:
            problem["input_output"] = json.load(f)
    else:
        problem["input_output"] = None

    # Read solutions.json
    solutions_file = problem_dir / 'solutions.json'
    if solutions_file.exists():
        with open(solutions_file, 'r') as f:
            problem["solutions"] = json.load(f)
    else:
        problem["solutions"] = None

    # Read starter_code.py if it exists, otherwise set it to None
    starter_code_file = problem_dir / 'starter_code.py'
    if starter_code_file.exists():
        with open(starter_code_file, 'r') as f:
            problem["starter_code"] = f.read().strip()
    else:
        problem["starter_code"] = None

    return problem

# Main function to generate code using LLM and save the results
def get_code(data_dir: Path, model: Model, output_file: Path, limit=150):
    output_file.parent.mkdir(parents=True, exist_ok=True)

    i = -1
    results = []
    for problem_dir in sorted(data_dir.iterdir()):
        if i == limit:
            break
        else:
            i += 1

         # Load data for each problem from its directory
        problem_data = load_problem_data(problem_dir)

        test_case = problem_data["input_output"]
        prompt = problem_data["question"]
        order_ignored = analyze_order_sensitivity(prompt, model)
        case_ignored = analyze_case_sensitivity(prompt, model)
        starter_code = problem_data["starter_code"]

        # If either the prompt or test case is missing, skip this problem
        if not prompt or not test_case:
            print(f"Skipping {problem_dir.name} due to missing data.")
            continue

        formatted_prompt = generate_prompt(test_case, prompt, starter_code)

        # Query the LLM to generate code
        response = model.query(formatted_prompt)

        # Extract the generated code from the LLM response
        generated_code = extract_code_from_response(response)

        test_inputs = test_case["inputs"]
        test_outputs = test_case["outputs"]

        # Execute tests on the generated code and calculate the pass rate, we give as argument the inputs the ouputs that are expeted and the generated code we need to test
        passed_tests, total_tests, counterexample = execute_tests(test_inputs, test_outputs, generated_code, order_ignored, case_ignored)
        pass_rate = passed_tests / total_tests if total_tests > 0 else 0

        result = {
            'task_id': problem_dir.name,
            'question': prompt,
            'generated_code': generated_code,
            'pass_rate': pass_rate,
            'passed_tests': passed_tests,
            'total_tests': total_tests,
            'counterexample': counterexample,
            'order_ignored': order_ignored,
            'case_ignored': case_ignored
        }
        results.append(result)
        print("*" * 100)
        print(f"Pass test: {passed_tests}/{total_tests}")
        print(f"Finished task: {problem_dir.name}")

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print(f"Results saved to {output_file}")

# Function to extract the generated code from the LLM response
def extract_code_from_response(response_content: str) -> str:
    code_pattern = r"```(?:[Pp]ython)?\n(.*?)```"
    match = re.search(code_pattern, response_content, re.DOTALL)
    if match:
        return match.group(1)
    return response_content


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="APPS code generation")
    parser.add_argument('--save', type=str, help="Directory to save result")

    args = parser.parse_args()

    # This path is missing from the git repo 
    data_dir = Path("APPS") / "test"
    output_dir = Path(args.save) if args.save else Path('data')

    model_name = "meta/llama-3.1-70b-instruct"
    model = get_model(model_name, 0.7)

    timestamp = datetime.now().strftime("%Y%m%d")
    output_file = output_dir / f"apps_{model_name}_{timestamp}.json"

    get_code(data_dir, model, output_file, 300)