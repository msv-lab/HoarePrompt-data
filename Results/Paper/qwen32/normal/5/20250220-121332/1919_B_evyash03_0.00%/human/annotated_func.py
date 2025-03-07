#State of the program right berfore the function call: expression is a string consisting of characters "+" and "-", and length is an integer representing the length of the string such that length = len(expression) and 1 <= length <= 5000.
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
        
    #State: `count` is the number of times the balance went negative, and `balance` is the final net balance after all resets.
    return count + (balance > 0)
    #The program returns the number of times the balance went negative plus 1 if the final net balance is greater than 0, otherwise it returns just the number of times the balance went negative.
#Overall this is what the function does:The function calculates the number of times a balance goes negative as it processes a string of "+" and "-" characters. If the final balance is positive, it adds one to the count of negative balances before returning the result. Otherwise, it returns the count of negative balances.

