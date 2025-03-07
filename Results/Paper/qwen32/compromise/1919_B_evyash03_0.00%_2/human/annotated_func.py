#State of the program right berfore the function call: expression is a string consisting of characters '+' and '-', and length is an integer such that length = len(expression) and 1 <= length <= 5000.
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
        
    #State: expression is a string consisting of characters '+' and '-', and length is an integer such that length = len(expression) and 1 <= length <= 5000; `count` is the number of times the balance went negative during the loop; `balance` is 0.
    return count + (balance > 0)
    #The program returns the number of times the balance went negative during the loop plus 1 if the balance is greater than 0 at the end of the loop.
#Overall this is what the function does:The function evaluates a string `expression` consisting of '+' and '-' characters and returns the number of times the cumulative balance of '+' and '-' went negative during the evaluation, plus one if the balance is positive at the end.

