#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 100), and s is a string of length n consisting only of the characters '+' and '-'.
def func():
    n = int(input())
    s = input()
    stones = 0
    for operation in s:
        if operation == '+':
            stones += 1
        elif operation == '-':
            stones = max(0, stones - 1)
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `s` is a string of length `n` consisting of '+' and '-', `stones` is the net result of applying all operations in `s`, which can range from 0 to `n` depending on the balance of '+' and '-' operations.
    print(stones)
#Overall this is what the function does:The function accepts a positive integer `n` and a string `s` consisting of `n` characters that are either '+' or '-'. It calculates the net number of "stones" based on the operations defined in the string, where each '+' increases the number of stones by 1 and each '-' decreases it by 1, ensuring that the number of stones never goes below 0. Finally, it prints the resulting number of stones.

