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
        
    #State of the program after the  for loop has been executed: `x` is an input integer such that 1 ≤ `x` ≤ 10^18; `max_sum` is the maximum digit sum of numbers from 1 to `x`; `max_num` is the number that produced `max_sum`.
    print(max_num)
#Overall this is what the function does:The function accepts no parameters and prompts the user for a positive integer `x` (1 ≤ x ≤ 10^18). It calculates the number between 1 and `x` that has the highest sum of its digits, and prints that number. If there are multiple numbers with the same maximum digit sum, it will print the first one encountered. However, the function does not handle any invalid input cases (e.g., if the input is not a valid integer or is outside the specified range).

