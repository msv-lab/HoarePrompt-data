#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100, and s is a string of length n consisting only of the characters '+' and '-', representing the operations performed by Vasya.
def func():
    n = int(input())
    s = input()
    stones = 0
    for operation in s:
        if operation == '+':
            stones += 1
        elif operation == '-':
            stones = max(0, stones - 1)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 <= `n` <= 100, `s` is a string of length `n` consisting only of the characters '+' and '-', `stones` is equal to the net result of the operations in `s`, which is the count of '+' minus the count of '-' but not less than 0.
    print(stones)
#Overall this is what the function does:The function accepts a positive integer `n` and a string `s` of length `n` consisting of the characters '+' and '-'. It processes the operations represented by the string to calculate a count of "stones", where each '+' increases the count by 1 and each '-' decreases the count by 1, ensuring that the count does not fall below 0. The final count of stones is printed as the output.

