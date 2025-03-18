#State of the program right berfore the function call: expression is a string of length `length` consisting only of characters "+" and "-", and `length` is a positive integer such that 1 ≤ length ≤ 5000.
def func_1(expression, length):
    count = 0
    for char in expression:
        if char == '+':
            count += 1
        
    #State: `expression` is a non-empty string of length `length` (1 ≤ length ≤ 5000) consisting only of characters "+" and "-", `count` is the number of "+" characters in `expression`.
    sub = length - count
    return abs(sub - count)
    #The program returns the absolute difference between the number of "-" characters (`sub`) and the number of "+" characters (`count`) in the string `expression`.
#Overall this is what the function does:The function `func_1` takes a string `expression` and an integer `length` as inputs. The string `expression` consists only of the characters "+" and "-", and its length is between 1 and 5000. The function calculates the absolute difference between the number of "+" characters and the number of "-" characters in the `expression` and returns this value. After the function concludes, the final state is that the function has returned an integer representing this absolute difference.

