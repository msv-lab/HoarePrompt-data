#State of the program right berfore the function call: The input is a string representing a positive integer x, where 1 ≤ x ≤ 10^18.
def func():
    x = int(input())
    max_sum = 0
    max_num = 0
    for i in range(1, x + 1):
        digit_sum = sum(int(digit) for digit in str(i))
        
        if digit_sum > max_sum:
            max_sum = digit_sum
            max_num = i
        
    #State of the program after the  for loop has been executed: `max_sum` is the maximum digit sum of any integer between 1 and `x`, `max_num` is the integer between 1 and `x` that has this maximum digit sum.
    print(max_num)
#Overall this is what the function does:The function accepts a string representing a positive integer \( x \), where \( 1 \leq x \leq 10^{18} \). It then iterates through all integers from 1 to \( x \), calculating the sum of the digits of each integer. The function identifies the integer within this range whose digit sum is the highest and prints this integer. The function handles the edge case where \( x \) is the smallest possible value (1), as the digit sum of 1 is 1, which is the maximum possible digit sum for numbers up to 1. There is no missing functionality in the provided code.

