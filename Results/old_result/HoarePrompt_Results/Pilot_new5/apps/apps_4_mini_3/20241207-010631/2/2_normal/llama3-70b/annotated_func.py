#State of the program right berfore the function call: x is a positive integer such that 1 ≤ x ≤ 10^18.
def func():
    x = int(input())
    max_sum = 0
    max_num = 0
    for i in range(1, x + 1):
        digit_sum = sum(int(digit) for digit in str(i))
        
        if digit_sum > max_sum:
            max_sum = digit_sum
            max_num = i
        
    #State of the program after the  for loop has been executed: `x` is an input integer such that 1 ≤ `x` ≤ 10^18, `max_sum` is the maximum digit sum of all integers from 1 to `x`, `max_num` is the integer from 1 to `x` that has the maximum digit sum.
    print(max_num)
#Overall this is what the function does:The function reads a positive integer `x` from user input, where 1 ≤ `x` ≤ 10^18. It calculates the integer from 1 to `x` that has the maximum digit sum and prints that integer. The function does not return any value.

