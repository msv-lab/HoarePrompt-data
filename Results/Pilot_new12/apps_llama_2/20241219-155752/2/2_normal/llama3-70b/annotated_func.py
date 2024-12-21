#State of the program right berfore the function call: x is a positive integer between 1 and 10^18 inclusive.
def func():
    x = int(input())
    max_sum = 0
    max_num = 0
    for i in range(1, x + 1):
        digit_sum = sum(int(digit) for digit in str(i))
        
        if digit_sum > max_sum:
            max_sum = digit_sum
            max_num = i
        
    #State of the program after the  for loop has been executed: `x` is the original input integer, `max_sum` is the maximum sum of digits of any number from 1 to `x`, and `max_num` is the number from 1 to `x` whose digits sum up to `max_sum`. If `x` is less than or equal to 0, then `max_sum` is 0 and `max_num` is 0.
    print(max_num)
#Overall this is what the function does:The function accepts no parameters and returns the number between 1 and the input integer (inclusive) whose digits sum up to the maximum possible sum, or 0 if the input integer is less than or equal to 0. It prints this number as output. After execution, the function's state is such that it has determined the maximum sum of digits of any number from 1 to the input integer and the corresponding number that yields this maximum sum, handling edge cases where the input integer may be outside the expected range of positive integers between 1 and 10^18. If the input integer is not within the expected range, the function may still produce a result based on the provided input.

