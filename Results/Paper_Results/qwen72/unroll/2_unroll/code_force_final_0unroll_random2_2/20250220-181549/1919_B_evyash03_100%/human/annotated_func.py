#State of the program right berfore the function call: expression is a string of length length, consisting only of the characters "+" and "-", and length is a positive integer such that 1 <= length <= 5000.
def func_1(expression, length):
    count = 0
    for char in expression:
        if char == '+':
            count += 1
        
    #State: `count` is the number of "+" characters in `expression`.
    sub = length - count
    return abs(sub - count)
    #The program returns the absolute difference between `sub` and `count`, where `sub` is equal to `length - count` and `count` is the number of "+" characters in `expression`.
#Overall this is what the function does:The function `func_1` accepts a string `expression` and an integer `length`. It calculates the number of "+" characters in `expression` and returns the absolute difference between this count and the number of "-" characters in `expression`. The final state of the program is that it has returned this absolute difference as an integer.

