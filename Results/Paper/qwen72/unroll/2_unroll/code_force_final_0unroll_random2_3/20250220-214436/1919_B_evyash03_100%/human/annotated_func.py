#State of the program right berfore the function call: expression is a string consisting only of '+' and '-' characters, and length is a positive integer such that 1 <= length <= 5000 and length equals the length of expression.
def func_1(expression, length):
    count = 0
    for char in expression:
        if char == '+':
            count += 1
        
    #State: `count` is the number of '+' characters in `expression`, `length` remains the same, and `expression` remains unchanged.
    sub = length - count
    return abs(sub - count)
    #The program returns the absolute value of the difference between `sub` and `count`, where `sub` is equal to `length - count` and `count` is the number of '+' characters in `expression`.
#Overall this is what the function does:The function `func_1` accepts a string `expression` containing only '+' and '-' characters, and an integer `length` that matches the length of `expression`. It returns the absolute value of the difference between the number of '-' characters and the number of '+' characters in `expression`. The input parameters `expression` and `length` remain unchanged after the function call.

