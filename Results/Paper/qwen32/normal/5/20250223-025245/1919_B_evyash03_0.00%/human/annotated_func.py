#State of the program right berfore the function call: expression is a string consisting of '+' and '-' characters, and length is a positive integer representing the length of the string expression such that length == len(expression).
def func_1(expression, length):
    count = 0
    balance = 0
    for char in expression:
        if char == '+':
            balance += 1
        elif char == '-':
            balance -= 1
        
        if balance < 0:
            count += 1
            balance = 0
        
    #State: expression is a string consisting of '+' and '-' characters with length `length`; `length` is a positive integer such that `length == len(expression)`; `count` is the number of times `balance` was negative and reset to 0; `balance` is 0.
    return count + (balance > 0)
    #The program returns the number of times `balance` was negative and reset to 0, plus 1 if `balance` is currently greater than 0.
#Overall this is what the function does:The function takes a string `expression` consisting of '+' and '-' characters and a positive integer `length` representing the length of the string. It returns the number of times the cumulative balance of '+' and '-' characters became negative and was reset to zero, plus one if the final balance is positive.

