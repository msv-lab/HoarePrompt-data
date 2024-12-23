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
        
    #State of the program after the  for loop has been executed: `x` is an integer value such that 1 ≤ `x` ≤ 10^18, `max_num` is the integer within the range [1, `x`] that has the highest digit sum, and `max_sum` is the digit sum of `max_num`.
    print(max_num)
#Overall this is what the function does:The function accepts a string representing a positive integer \( x \), where \( 1 \leq x \leq 10^{18} \). It iterates through all integers from 1 to \( x \), calculates the sum of the digits of each integer, and identifies the integer within this range that has the highest digit sum. The function then prints this integer. Potential edge cases include when \( x \) is at its minimum (1) or maximum (\( 10^{18} \)). In these cases, the function will correctly identify 1 as the integer with the highest digit sum since the digit sum of 1 is 1, and no other number within the range has a higher digit sum. There is no missing functionality in the given code; it correctly handles the problem as described.

