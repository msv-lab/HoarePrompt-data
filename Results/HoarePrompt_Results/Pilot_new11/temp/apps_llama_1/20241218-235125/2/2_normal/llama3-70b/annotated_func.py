#State of the program right berfore the function call: No input variables are explicitly defined in the function, but based on the problem description, we can infer that the function should operate on a positive integer x, such that 1 ≤ x ≤ 10^18.
def func():
    x = int(input())
    max_sum = 0
    max_num = 0
    for i in range(1, x + 1):
        digit_sum = sum(int(digit) for digit in str(i))
        
        if digit_sum > max_sum:
            max_sum = digit_sum
            max_num = i
        
    #State of the program after the  for loop has been executed: `x` is a positive integer, `i` is equal to `x`, `max_sum` is the maximum sum of digits of any number in the range from 1 to `x`, and `max_num` is the number in the range from 1 to `x` whose digits sum up to `max_sum`.
    print(max_num)
#Overall this is what the function does:The function accepts a positive integer input from the user, calculates the sum of digits for each number in the range from 1 to the input number, and returns the number whose digits sum up to the maximum value. If there are multiple numbers with the same maximum sum of digits, it returns the first one encountered in the range. The function handles input values ranging from 1 to 10^18, although it may be limited by the system's input processing capabilities. The function does not handle non-integer or non-positive inputs, which may cause it to fail or produce incorrect results. After execution, the program's state is defined by the output of the maximum number, and the input variable is discarded. The function does not modify any external state or have any side effects beyond printing the result.

