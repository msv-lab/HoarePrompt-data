#State of the program right berfore the function call: n is a positive integer (1 <= n <= 100), and s is a string of length n consisting of symbols '+' and '-' only.
def func():
    n = int(input())
    s = input()
    stones = 0
    for operation in s:
        if operation == '+':
            stones += 1
        elif operation == '-':
            stones = max(0, stones - 1)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 <= n <= 100), `s` is a string of length `n` consisting of symbols '+' and '-' only, `stones` is equal to `max(0, (number of '+' in s) - (number of '-' in s))`.
    print(stones)
#Overall this is what the function does:The function accepts a positive integer `n` (where 1 <= n <= 100) and a string `s` of length `n`, consisting of symbols '+' and '-'. It calculates the final number of "stones" by incrementing for each '+' and decrementing for each '-' but ensures that the number of stones does not go below zero. Finally, it prints the result, which corresponds to the maximum of zero and the difference between the counts of '+' and '-' operations.

