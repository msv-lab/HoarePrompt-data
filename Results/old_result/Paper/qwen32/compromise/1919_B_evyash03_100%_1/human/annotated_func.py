#State of the program right berfore the function call: expression is a string consisting of the characters "+" and "-", and length is an integer such that length = len(expression) and 1 <= length <= 5000.
def func_1(expression, length):
    count = 0
    for char in expression:
        if char == '+':
            count += 1
        
    #State: count is the number of '+' characters in the expression.
    sub = length - count
    return abs(sub - count)
    #The program returns the absolute value of the difference between the length of the expression minus the number of '+' characters and the number of '+' characters.
#Overall this is what the function does:The function calculates and returns the absolute difference between the number of '-' characters and the number of '+' characters in the given expression string.

