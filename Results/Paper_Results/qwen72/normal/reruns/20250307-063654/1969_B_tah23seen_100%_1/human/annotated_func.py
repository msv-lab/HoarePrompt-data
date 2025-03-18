#State of the program right berfore the function call: s is a binary string (a string consisting of only 0s and 1s) with a length of at least 2 and at most 200,000.
def func_1(s):
    cost = 0
    one = 0
    for i in s:
        if i == '1':
            one += 1
        elif i == '0' and one > 0:
            cost += one + 1
        
    #State: After all iterations, `s` remains a binary string with a length of at least 2 and at most 200,000. `one` is the count of '1's in the string `s` that are not followed by a '0'. `cost` is the total sum of `one + 1` for each '0' in the string `s` that is preceded by at least one '1'.
    return cost
    #The program returns the total sum of `one + 1` for each '0' in the string `s` that is preceded by at least one '1', where `one` is the count of '1's in the string `s` that are not followed by a '0'.
#Overall this is what the function does:The function `func_1` accepts a binary string `s` and returns an integer `cost`. The `cost` is calculated as the total sum of `one + 1` for each '0' in the string `s` that is preceded by at least one '1', where `one` is the count of consecutive '1's in the string that are not immediately followed by a '0'. The original string `s` remains unchanged after the function execution.

