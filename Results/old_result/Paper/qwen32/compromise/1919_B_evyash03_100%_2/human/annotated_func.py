#State of the program right berfore the function call: expression is a string consisting of the characters '+' and '-', and length is a positive integer representing the length of the string such that length == len(expression).
def func_1(expression, length):
    count = 0
    for char in expression:
        if char == '+':
            count += 1
        
    #State: expression is a string consisting of the characters '+' and '-', length is a positive integer representing the length of the string such that length == len(expression), count is the number of '+' characters in the string expression.
    sub = length - count
    return abs(sub - count)
    #The program returns the absolute difference between the number of '-' characters and the number of '+' characters in the string `expression`.
#Overall this is what the function does:The function calculates and returns the absolute difference between the number of '-' characters and the number of '+' characters in the input string `expression`.

