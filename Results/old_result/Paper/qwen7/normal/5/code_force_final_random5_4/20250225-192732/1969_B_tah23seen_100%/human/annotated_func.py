#State of the program right berfore the function call: s is a binary string (a string consisting of only '0's and/or '1's) with a length between 2 and 200000.
def func_1(s):
    cost = 0
    one = 0
    for i in s:
        if i == '1':
            one += 1
        elif i == '0' and one > 0:
            cost += one + 1
        
    #State: After the loop executes all iterations, `s` is an empty string, `one` is the total count of '1's in the original string, and `cost` is the sum of `one + 1` for each '0' encountered in `s` where `one` is greater than 0, plus the initial cost of 2 for each iteration where `i` is '1'.
    return cost
    #The program returns the sum of (one + 1) for each '0' encountered in 's' where 'one' is greater than 0, plus an initial cost of 2 for each iteration where 'i' is '1'.
#Overall this is what the function does:The function accepts a binary string `s` and returns a cost calculated as follows: for each '0' in `s` where the count of preceding '1's (`one`) is greater than 0, it adds `one + 1` to the cost. Additionally, for each '1' in `s`, it adds 2 to the cost.

