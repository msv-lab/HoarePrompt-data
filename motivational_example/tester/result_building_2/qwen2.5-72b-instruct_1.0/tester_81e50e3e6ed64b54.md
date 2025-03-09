Your task is to generate a Python script with assertions to test the correctness of a given Python program, based on the provided problem description. Assume valid inputs as described in the problem description.

The output must be a complete Python with the assertions that verify the program’s correctness. Try to predict the program output yourslef for the expected values of the assertions , do not use the program code to calculate the expected value since errors can be duplicated. Do not execute the program yourself; just provide the test code.
If the code uses `stdin`, include the following helper function to automate input/output capture:

import io
import sys

def capture_output(func, input_data):
    sys.stdin = io.StringIO(input_data)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    func()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue().strip()


# Problem:
Given 5 non empty lists representing:
the number of first-semester students per class at Building A 
the number of administarators per class at Building A 
the number of first-semester students per class at Building B
the number of administarators per class at Building B
the number of professors per class at building B
there are 12 classes at building A and 16 at building B. ALl classes have duifferent number of people.
Make the building have equal number of people by removing the extra people from the more populous building.
Calculate a equal bonus for each moved person. The bonus pool is created by every staying person at both buildings contributing $10.
return the bonus that was given at each mover

# Program:
def func_1(students_A, admins_A, students_B, admins_B, profs_B):
    total_A = sum(students_A) + sum(admins_A)
    total_B = sum(students_B) + sum(admins_B) + sum(profs_B)
    surplus = abs(total_A - total_B)
    stayers = total_A + total_B - surplus
    bonus_pool = stayers * 10
    bonus_per_moved = bonus_pool / surplus
    return bonus_per_moved



# Your response:
```python
# Include necessary imports if any
# Assume the provided program is saved as 'program.py' and can be imported from the same dir.

from program import *

# Write your test cases below
# Each test case should include assertions based on the problem description
# Example:
# assert function_name(input) == expected_output

# Add multiple test cases to ensure correctness across edge cases
assert ...

# End of script
