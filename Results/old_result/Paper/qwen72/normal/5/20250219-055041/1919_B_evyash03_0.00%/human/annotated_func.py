#State of the program right berfore the function call: expression is a string of length length, where length is a positive integer (1 ≤ length ≤ 5000), and expression consists only of the characters '+' and '-'.
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
        
    #State: `expression` is a string of length `length` (1 ≤ `length` ≤ 5000) consisting only of the characters '+' and '-', `count` is the number of times `balance` went below 0 during the entire loop execution, and `balance` is the final balance after processing all characters in `expression`.
    return count + (balance > 0)
    #The program returns the sum of `count` and 1 if the final `balance` is greater than 0, otherwise it returns `count`.
#Overall this is what the function does:The function `func_1` accepts a string `expression` of length `length` (1 ≤ length ≤ 5000) consisting only of '+' and '-' characters, and an integer `length`. It returns the number of times the balance (the cumulative count of '+' minus '-') went below zero during the processing of the string, plus 1 if the final balance is greater than zero.

