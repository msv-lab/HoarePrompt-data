#State of the program right berfore the function call: expression is a string of length length consisting of characters '+' and '-', and length is an integer such that 1 <= length <= 5000.
def func_1(expression, length):
    count = 0
    for char in expression:
        if char == '+':
            count += 1
        
    #State: expression is a string of length length consisting of characters '+' and '-', length is an integer such that 1 <= length <= 5000, count is the number of '+' characters in expression.
    sub = length - count
    return abs(sub - count)
    #The program returns the absolute value of (length - 2*count)
#Overall this is what the function does:The function takes a string `expression` consisting of '+' and '-' characters and its length `length`. It calculates the absolute difference between the length of the string and twice the number of '+' characters in the string, and returns this value.

