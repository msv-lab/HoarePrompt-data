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
        
    #State of the program after the  for loop has been executed: `max_sum` is the maximum digit sum obtained from any number between 1 and `x`, `max_num` is the corresponding number for that maximum digit sum, `x` is an integer satisfying 1 ≤ `x` ≤ 10^18.
    print(max_num)
#Overall this is what the function does:The function reads a positive integer `x` from user input (where 1 ≤ x ≤ 10^18) and computes the number between 1 and `x` that has the largest sum of its digits. It then prints this number. Note that the function does not return any value, but merely prints the result.

