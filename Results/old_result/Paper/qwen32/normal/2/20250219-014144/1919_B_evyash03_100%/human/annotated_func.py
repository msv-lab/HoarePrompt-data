#State of the program right berfore the function call: expression is a string of length length consisting of characters '+' and '-', and length is an integer such that 1 <= length <= 5000.
def func_1(expression, length):
    count = 0
    for char in expression:
        if char == '+':
            count += 1
        
    #State: count is the number of '+' characters in the expression.
    sub = length - count
    return abs(sub - count)
    #The program returns the absolute value of (length - 2*count)
#Overall this is what the function does:The function calculates and returns the absolute value of the difference between the length of the given expression and twice the number of '+' characters in the expression.

