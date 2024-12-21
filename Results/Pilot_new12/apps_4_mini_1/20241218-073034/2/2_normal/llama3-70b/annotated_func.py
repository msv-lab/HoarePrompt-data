#State of the program right berfore the function call: x is a positive integer such that 1 <= x <= 10^18.
def func():
    x = int(input())
    max_sum = 0
    max_num = 0
    for i in range(1, x + 1):
        digit_sum = sum(int(digit) for digit in str(i))
        
        if digit_sum > max_sum:
            max_sum = digit_sum
            max_num = i
        
    #State of the program after the  for loop has been executed: `x` is a positive integer such that 1 <= `x` <= 10^18, `max_sum` is the maximum digit sum of any number from 1 to `x`, `max_num` is the number whose digit sum is `max_sum`.
    print(max_num)
#Overall this is what the function does:The function reads a positive integer `x` from user input, where `1 <= x <= 10^18`. It calculates the maximum digit sum of all integers from 1 to `x` and identifies the first integer (from 1 to `x`) that has this maximum digit sum. After processing all numbers, the function prints the integer that has the maximum digit sum. Notably, the function does not handle input validation or scenarios where `x` is outside the specified range, which could lead to undefined behavior or errors in practical use.

