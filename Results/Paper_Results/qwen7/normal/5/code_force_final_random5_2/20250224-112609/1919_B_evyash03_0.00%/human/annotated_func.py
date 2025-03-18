#State of the program right berfore the function call: expression is a string consisting of characters "+" and "-", and length is an integer representing the length of the string expression such that 1 <= length <= 5000.
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
        
    #State: The final value of `count` will be the total number of times `balance` was reset to 0 because it became less than 0 during the iteration of the loop. The final value of `balance` will be the net result of adding 1 for each '+' and subtracting 1 for each '-' in the `expression` string.
    return count + (balance > 0)
    #The program returns the total number of times balance was reset to 0 because it became less than 0 during the iteration of the loop plus 1 if the final balance is greater than 0.
#Overall this is what the function does:The function accepts a string `expression` consisting of characters "+" and "-" and an integer `length` representing the length of `expression`. It counts the number of times the balance (initially set to 0) is reset to 0 because it becomes negative during the iteration of `expression`. Additionally, it adds 1 to the count if the final balance is greater than 0. The function returns this total count.

