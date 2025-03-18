#State of the program right berfore the function call: num is a non-negative integer.
def func_1(num):
    num_str = str(num)
    num_len = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_len
        
    #State of the program after the  for loop has been executed: To determine the output state of the loop after all iterations have finished, let's analyze the given information step by step.
    #
    #1. **Initial State**: 
    #   - `num` is a non-negative integer.
    #   - `num_str` is the string representation of `num`.
    #   - `num_len` is the number of digits in `num`.
    #   - `sum` is 0.
    #
    #2. **Loop Code**:
    #   ```
    #   for digit in num_str:
    #       sum += int(digit) ** num_len
    #   ```
    #   This loop iterates over each character (digit) in the string representation of `num`. For each digit, it converts the digit back to an integer, raises it to the power of `num_len` (the total number of digits in `num`), and adds this value to `sum`.
    #
    #3. **Understanding the Loop's Behavior**:
    #   - If `num` has 0 digits (which is the case when `num` is 0), `num_str` is "0", and `num_len` is 1. The loop will execute once, converting "0" to an integer, raising it to the power of 1, and adding 0 to `sum`. Thus, `sum` remains 0.
    #   - If `num` has 1 or more digits, the loop will execute for each digit. For each digit, it calculates the digit raised to the power of the total number of digits in `num` and adds this to `sum`.
    #   - The key observation is that `num_len` does not change within the loop, so each digit is raised to the same power, which is the total number of digits in `num`.
    #
    #4. **Determining the Output State**:
    #   - `num` remains unchanged as it is not modified within the loop.
    #   - `num_str` also remains unchanged as it is just a string representation of `num` and does not change within the loop.
    #   - `num_len` remains the same, as it is calculated before the loop and does not change within the loop.
    #   - `sum` will be the sum of each digit in `num` raised to the power of `num_len`. If `num` is 0, `sum` remains 0.
    #
    #Given this analysis, the output state after all iterations of the loop have finished can be summarized as follows:
    #
    #- If `num` is 0, `sum` is 0.
    #- If `num` is not 0, `sum` is the sum of each digit in `num` raised to the power of the total number of digits in `num`.
    #
    #**Output State: `num` is a non-negative integer, `num_str` is the string representation of `num`, `num_len` is the number of digits in `num`, `sum` is the sum of each digit in `num` raised to the power of `num_len`, or 0 if `num` is 0.**
    return sum == num
    #The program returns a boolean value (`True` or `False`) indicating whether the sum of each digit in `num` (a non-negative integer) raised to the power of `num_len` (the number of digits in `num`), or 0 if `num` is 0, is equal to `num`.
#Overall this is what the function does:The function accepts a non-negative integer `num`, calculates the sum of each digit in `num` raised to the power of the number of digits in `num`, and returns `True` if this sum equals `num`, and `False` otherwise, covering all potential cases including edge cases for 0 and single-digit numbers.

