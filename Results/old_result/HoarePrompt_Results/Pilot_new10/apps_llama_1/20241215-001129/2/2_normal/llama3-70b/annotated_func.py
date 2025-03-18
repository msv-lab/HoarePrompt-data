#State of the program right berfore the function call: The input is a positive integer x such that 1 ≤ x ≤ 10^18.
def func():
    x = int(input())
    max_sum = 0
    max_num = 0
    for i in range(1, x + 1):
        digit_sum = sum(int(digit) for digit in str(i))
        
        if digit_sum > max_sum:
            max_sum = digit_sum
            max_num = i
        
    #State of the program after the  for loop has been executed: `x` is a positive integer such that 1 ≤ `x` ≤ 10^18, `i` is equal to `x`, `digit_sum` is the sum of the digits of `x`, `max_sum` is the maximum sum of digits of any number from 1 to `x`, and `max_num` is the number from 1 to `x` that has `max_sum` as its sum of digits.
    print(max_num)
#Overall this is what the function does:The function prompts the user for a positive integer input `x`, calculates the sum of digits for each number from 1 to `x`, and prints the number with the maximum sum of digits; it assumes the input is valid and within the range 1 to 10^18, without explicitly handling edge cases of invalid inputs or very large numbers.

