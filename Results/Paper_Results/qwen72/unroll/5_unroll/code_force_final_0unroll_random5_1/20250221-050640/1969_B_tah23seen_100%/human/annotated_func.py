#State of the program right berfore the function call: s is a binary string (a string consisting of only '0's and '1's) with a length of 2 or more, and the length of s does not exceed 2 \cdot 10^5.
def func_1(s):
    cost = 0
    one = 0
    for i in s:
        if i == '1':
            one += 1
        elif i == '0' and one > 0:
            cost += one + 1
        
    #State: `s` remains a binary string with a length of 2 or more, `cost` is the total number of times '0' appears in `s` after a '1', each contributing `one + 1` to the cost, and `one` is the number of '1's in `s`.
    return cost
    #The program returns the total number of times '0' appears in `s` after a '1', each contributing `one + 1` to the cost, where `one` is the number of '1's in `s`.
#Overall this is what the function does:The function `func_1` accepts a binary string `s` and returns the total cost calculated by counting the number of '0's that appear after a '1' in the string, with each '0' contributing `one + 1` to the cost, where `one` is the number of '1's encountered before each '0'. The input string `s` remains unchanged.

