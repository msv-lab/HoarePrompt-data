#State of the program right berfore the function call: expression is a string consisting of characters "+" and "-", and length is a positive integer such that 1 <= length <= 5000 and length equals the length of expression.
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
        
    #State: `count` is the number of times the balance goes below 0 during the iteration of the expression, and `balance` is the final balance after all iterations.
    return count + (balance > 0)
    #The program returns the number of times the balance went below 0 during the iteration plus 1 if the final balance is greater than 0, otherwise it returns just the number of times the balance went below 0.
#Overall this is what the function does:The function `func_1` accepts a string `expression` consisting of characters "+" and "-" and an integer `length` that represents the length of `expression` (1 <= length <= 5000). It returns the number of times the balance (tracked by the number of "+" and "-" characters) goes below 0 during the iteration of the expression, plus 1 if the final balance is greater than 0. If the final balance is not greater than 0, it returns only the number of times the balance went below 0.

