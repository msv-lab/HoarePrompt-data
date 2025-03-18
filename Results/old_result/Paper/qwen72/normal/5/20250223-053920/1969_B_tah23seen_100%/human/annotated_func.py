#State of the program right berfore the function call: s is a binary string (a string consisting of only 0s and 1s) with a length of at least 2 and at most 200,000.
def func_1(s):
    cost = 0
    one = 0
    for i in s:
        if i == '1':
            one += 1
        elif i == '0' and one > 0:
            cost += one + 1
        
    #State: `s` remains a binary string with a length of at least 2 and at most 200,000, `cost` is the total number of '0's in `s` that come after at least one '1', each contributing a cost of the number of '1's seen so far plus one, and `one` is the total number of '1's in `s`.
    return cost
    #The program returns the total number of '0's in `s` that come after at least one '1', each contributing a cost of the number of '1's seen so far plus one.
#Overall this is what the function does:The function `func_1` accepts a binary string `s` and returns the total cost calculated based on the number of '0's in `s` that appear after at least one '1'. Each '0' contributes a cost equal to the number of '1's seen before it plus one. The input string `s` remains unchanged.

