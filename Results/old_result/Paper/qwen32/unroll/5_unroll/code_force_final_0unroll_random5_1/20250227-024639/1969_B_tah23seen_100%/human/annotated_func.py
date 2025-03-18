#State of the program right berfore the function call: s is a binary string (a string consisting of only '0's and '1's) with length between 2 and 200,000. The function `func_1` is called once for each test case, and the total length of all strings across all test cases does not exceed 200,000.
def func_1(s):
    cost = 0
    one = 0
    for i in s:
        if i == '1':
            one += 1
        elif i == '0' and one > 0:
            cost += one + 1
        
    #State: `s` is unchanged; `cost` is the sum of (number of consecutive '1's + 1) for each sequence of '1's followed by a '0'; `one` is the count of consecutive '1's at the end of the string `s` (if any).
    return cost
    #The program returns `cost`, which is the sum of (number of consecutive '1's + 1) for each sequence of '1's followed by a '0'.
#Overall this is what the function does:The function accepts a binary string `s` and returns a cost, which is the sum of (number of consecutive '1's + 1) for each sequence of '1's followed by a '0'.

