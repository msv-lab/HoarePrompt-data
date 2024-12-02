import subprocess

def compare_outputs(expected: str, got: str, ignore_order: bool = False, ignore_case: bool = False) -> bool:
    def normalize_output_sorted(output: str):
        lines = output.strip().splitlines()
        normalized_lines = []
        for line in lines:
            words = line.strip().split()
            if ignore_case:
                words = [word.lower() for word in words]
            normalized_lines.append(" ".join(sorted(words)))
        return sorted(normalized_lines)
    
    def normalize_output(output: str):
        lines = output.strip().splitlines()
        normalized_lines = []
        for line in lines:
            words = line.strip().split()
            if ignore_case:
                words = [word.lower() for word in words]
            normalized_lines.append(" ".join(words))
        return normalized_lines
    
    if ignore_order:
        return normalize_output_sorted(expected) == normalize_output_sorted(got)
    else:
        return normalize_output(expected) == normalize_output(got)

# Function to execute the generated Python code with the given input data
def execute_code(code_str: str, input_data: str):
    try:
        #It runs the Python code in a subprocess, passing the input_data, and capturing the output
        result = subprocess.run(['python3', '-c', code_str], input=input_data,
                                capture_output=True, text=True, timeout=3)
        return result.stdout, result.stderr
    # Handle the case where the execution takes too long and times out
    except subprocess.TimeoutExpired:
        return '', 'TimeoutError: Execution exceeded time limit'
    # Handles other exception
    except Exception as e:
        return '', str(e)

# We pass the expected output for an input to compare it with the output of running the genrated code
def execute_tests(inputs, outputs, generated_code, order_ignore, case_ignore):
    passed_tests = 0
    total_tests = len(inputs)
    failure_example = None

    for input_data, expected_output in zip(inputs, outputs):
        stdout, stderr = execute_code(generated_code, input_data)

         # If there is an error in execution (stderr), record the failure
        if stderr:
            if failure_example is None:
                failure_example = {"input": input_data, "expected": expected_output, "got": stderr.strip()}
        else:
            # Compare the output of the code with the expected output
            if compare_outputs(stdout.strip(), expected_output.strip(), order_ignore, case_ignore):
                passed_tests += 1
            else:
                # If the output does not match, record the failure
                if failure_example is None:
                    failure_example = {"input": input_data, "expected": expected_output, "got": stdout.strip()}
       
    # Return the number of passed tests, the total number of tests, and the first failure example
    return passed_tests, total_tests, failure_example
