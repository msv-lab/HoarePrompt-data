#State of the program right berfore the function call: expression is a string of length length consisting of characters "+" and "-", and length is an integer such that 1 <= length <= 5000.
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
        
    #State: expression is a string of length length consisting of characters "+" and "-", length is an integer such that 1 <= length <= 5000, count is the number of times balance went negative and was reset to 0, balance is the final non-negative value after all operations.
    return count + (balance > 0)
    #The program returns the sum of the number of times the balance went negative and was reset to 0, and 1 if the final balance is greater than 0, otherwise 0.
#Overall this is what the function does:The function evaluates a string `expression` consisting of '+' and '-' characters, and returns the sum of the number of times the cumulative balance (starting at 0, incremented by 1 for each '+', decremented by 1 for each '-') went negative and was reset to 0, plus 1 if the final balance is greater than 0.

