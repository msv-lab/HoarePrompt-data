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
        
    #State of the program after the  for loop has been executed: `max_sum` is the maximum digit sum from numbers 1 to `x`, `max_num` is the number that produces `max_sum`, `x` is a positive integer such that 1 ≤ `x` ≤ 10^18.
    print(max_num)
#Overall this is what the function does:The function accepts a positive integer input from the user and calculates the maximum digit sum of the numbers from 1 to that integer. It identifies the number that yields this maximum digit sum and prints that number.

