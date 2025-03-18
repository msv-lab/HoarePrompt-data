#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100, and s is a string of length n consisting of the symbols '+' and '-'.
def func():
    n = int(input())
    s = input()
    stones = 0
    for operation in s:
        if operation == '+':
            stones += 1
        elif operation == '-':
            stones = max(0, stones - 1)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 <= `n` <= 100, `s` is a string of length equal to `n`, and `stones` is the result of applying all operations in `s` starting from 0, where `stones` can never be less than 0.
    print(stones)
#Overall this is what the function does:The function accepts a positive integer `n` (where \( 1 \leq n \leq 100 \)) and a string `s` of length `n` consisting of the symbols '+' and '-'. It calculates the net result of operations on a counter starting from 0, incrementing the counter by 1 for each '+' and decrementing it by 1 for each '-' without allowing the counter to go below 0. Finally, it prints the resulting number of stones after all operations have been applied.

