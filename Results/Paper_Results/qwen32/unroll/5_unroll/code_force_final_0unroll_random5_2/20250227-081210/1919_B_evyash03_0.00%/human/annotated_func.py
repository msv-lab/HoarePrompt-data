#State of the program right berfore the function call: expression is a string consisting of characters '+' and '-', and length is a positive integer such that length equals the length of the string expression.
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
        
    #State: expression is "+--++-", length is 6, count is 1, balance is 1.
    return count + (balance > 0)
    #The program returns 2
#Overall this is what the function does:The function calculates the number of times the balance of '+' and '-' characters in the string `expression` goes negative, resets it to zero, and finally adds one if there is a positive balance left. The function returns this calculated value.

