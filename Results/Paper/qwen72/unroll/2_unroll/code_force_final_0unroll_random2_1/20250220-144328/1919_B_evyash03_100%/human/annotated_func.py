#State of the program right berfore the function call: expression is a string consisting only of characters "+" and "-", and length is a positive integer such that 1 <= length <= 5000 and length is equal to the length of expression.
def func_1(expression, length):
    count = 0
    for char in expression:
        if char == '+':
            count += 1
        
    #State: `count` is the number of "+" characters in `expression`.
    sub = length - count
    return abs(sub - count)
    #The program returns the absolute difference between the number of integers in the expression and the number of "+" characters in the expression.
#Overall this is what the function does:The function `func_1` accepts a string `expression` consisting only of "+" and "-" characters, and an integer `length` equal to the length of `expression`. It returns the absolute difference between the number of "+" characters and the number of "-" characters in the `expression`.

