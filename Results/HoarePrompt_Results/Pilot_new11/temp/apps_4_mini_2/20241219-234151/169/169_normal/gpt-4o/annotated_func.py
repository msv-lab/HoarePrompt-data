#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100, and s is a string consisting of n characters, each character being either '-' or '+'.
def func():
    n = int(input())
    s = input()
    stones = 0
    for operation in s:
        if operation == '+':
            stones += 1
        elif operation == '-':
            stones = max(0, stones - 1)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= `n` <= 100, `s` is a string of length `n` consisting of '-' or '+' characters; `stones` is equal to the net effect of all operations in `s`, representing the count of stones accumulated, with a minimum value of 0.
    print(stones)
#Overall this is what the function does:The function reads a positive integer `n` and a string `s` of length `n` from the input, which consists exclusively of the characters '-' and '+'. It processes the string to calculate the total number of 'stones' based on these rules: each '+' increments a counter (stones) by 1, while each '-' decrements it by 1, ensuring that the counter does not drop below 0. After processing the string, the function prints the final count of stones. The function effectively handles edge cases, such as multiple consecutive '-' characters, by ensuring that stones do not become negative. However, it assumes valid input as per the specified constraints but does not handle cases where input does not meet those constraints.

