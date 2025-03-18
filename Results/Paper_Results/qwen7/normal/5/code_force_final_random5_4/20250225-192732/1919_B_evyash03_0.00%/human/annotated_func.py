#State of the program right berfore the function call: expression is a string of length n consisting of characters "+" and "-", and length is an integer representing the length of the string expression.
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
        
    #State: Output State: The entire `expression` string has been processed, `balance` is 0, `count` is equal to the number of times `balance` became negative during the iteration of the `expression`, and `char` will be the first character of the `expression` since it would have been the last character checked before the loop terminated.
    #
    #In simpler terms, after the loop completes all its iterations, the `expression` string will be fully processed, `balance` will be 0 (indicating that any initial imbalance has been corrected), `count` will hold the total number of times `balance` went below zero, and `char` will be the first character of the original `expression`.
    return count + (balance > 0)
    #The program returns the value of count.
#Overall this is what the function does:The function accepts a string `expression` consisting of "+" and "-" characters and an integer `length` (though `length` is not used in the function). It counts the number of times the balance (difference between the number of "+" and "-") becomes negative while iterating through the string. The function returns this count plus one if the final balance is positive, otherwise just the count.

