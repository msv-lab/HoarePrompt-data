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
        
    #State of the program after the  for loop has been executed: `max_sum` is the maximum digit sum of numbers from 1 to `x`, `max_num` is the number whose digits sum to `max_sum`, `x` is the input integer such that 1 ≤ `x` ≤ 10^18.
    print(max_num)
#Overall this is what the function does:The function reads a positive integer input \( x \) (where \( 1 \leq x \leq 10^{18} \)) and calculates the number (\( \text{max\_num} \)) between 1 and \( x \) that has the highest digit sum. It sums the individual digits of each number from 1 to \( x \) and keeps track of the maximum digit sum found (\( \text{max\_sum} \)). After examining all numbers in this range, it prints the number that has the maximum digit sum. Note that if multiple numbers have the same maximum digit sum, the function will return the first such number encountered. Importantly, this function does not return any values or accept parameters; it directly reads input and prints an output. The function does not handle invalid inputs or edge cases such as non-integer inputs or integers outside the specified range.

