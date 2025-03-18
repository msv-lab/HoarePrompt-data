#State of the program right berfore the function call: expression is a string consisting of characters "+" and "-" only, and length is a positive integer such that 1 <= length <= 5000 and length == len(expression).
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
        
    #State: `count` is the number of times the balance goes below zero, and `balance` is the final balance after processing all characters in `expression`.
    return count + (balance > 0)
    #The program returns the number of times the balance goes below zero (`count`) plus 1 if the final balance (`balance`) is greater than 0, otherwise it returns `count` unchanged.
#Overall this is what the function does:The function `func_1` accepts a string `expression` consisting of "+" and "-" characters and a positive integer `length` that matches the length of `expression`. It returns the number of times the balance (tracked by the number of "+" and "-" characters) goes below zero during the processing of the string, plus 1 if the final balance is greater than 0. If the final balance is not greater than 0, the function returns the number of times the balance went below zero.

