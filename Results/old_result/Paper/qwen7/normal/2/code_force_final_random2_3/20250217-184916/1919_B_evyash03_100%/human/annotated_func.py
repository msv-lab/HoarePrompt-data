#State of the program right berfore the function call: expression is a string of length n consisting of characters "+" and "-", and length is an integer representing the length of the string expression.
def func_1(expression, length):
    count = 0
    for char in expression:
        if char == '+':
            count += 1
        
    #State: The loop has executed all iterations, meaning `count` is equal to the length of the string `expression`. The string `expression` remains unchanged, and `count` holds the total number of '+' characters in `expression`.
    sub = length - count
    return abs(sub - count)
    #The program returns the absolute difference between the length of `expression` minus the total number of '+' characters in `expression`, and the total number of '+' characters in `expression`
#Overall this is what the function does:The function `func_1` accepts two parameters: `expression`, a string consisting of '+' and '-' characters, and `length`, an integer representing the length of `expression`. It calculates and returns the absolute difference between the length of `expression` and twice the number of '+' characters in `expression`.

