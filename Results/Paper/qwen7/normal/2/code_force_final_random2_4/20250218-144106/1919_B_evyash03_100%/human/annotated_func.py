#State of the program right berfore the function call: expression is a string of length n consisting of characters "+" and "-", and length is an integer representing the length of the string expression such that 1 <= length <= 5000.
def func_1(expression, length):
    count = 0
    for char in expression:
        if char == '+':
            count += 1
        
    #State: The final value of `count` will be equal to the total number of '+' characters in the string `expression`.
    sub = length - count
    return abs(sub - count)
    #The program returns the absolute difference between the value of `sub` (which is `length - count`) and `count`
#Overall this is what the function does:The function accepts a string `expression` consisting of "+" and "-" characters, along with its length `length`. It counts the number of "+" characters in `expression` and calculates the number of "-" characters as the difference between `length` and the count of "+". Finally, it returns the absolute difference between these two counts.

