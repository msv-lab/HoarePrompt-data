#State of the program right berfore the function call: s is a binary string (consisting of only '0's and '1's) with a length of 2 to 200,000 characters.
def func_1(s):
    cost = 0
    one = 0
    for i in s:
        if i == '1':
            one += 1
        elif i == '0' and one > 0:
            cost += one + 1
        
    #State: `s` remains unchanged, `cost` is the total number of '0's in `s` multiplied by the number of '1's before each '0' plus the number of '0's, `one` is the total number of '1's in `s`.
    return cost
    #The program returns the total number of '0's in `s` multiplied by the number of '1's before each '0' plus the number of '0's.
#Overall this is what the function does:The function `func_1` accepts a binary string `s` and returns a value that represents the total number of '0's in `s` multiplied by the number of '1's that appear before each '0', plus the total number of '0's in `s`. The input string `s` remains unchanged after the function execution.

