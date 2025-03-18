#State of the program right berfore the function call: s is a binary string (a string consisting of only '0's and/or '1's) with a length between 2 and 200000.
def func_1(s):
    cost = 0
    one = 0
    for i in s:
        if i == '1':
            one += 1
        elif i == '0' and one > 0:
            cost += one + 1
        
    #State: Output State: `s` is a binary string, `cost` is the total cost calculated based on the conditions in the loop, `one` is the count of consecutive '1's encountered before encountering a '0'.
    return cost
    #The program returns the total cost calculated based on the conditions in the loop
#Overall this is what the function does:The function accepts a binary string `s` and calculates the total cost based on the conditions in the loop. For each '0' encountered, if there have been any consecutive '1's before it, the cost increases by the number of those '1's plus one. The function returns the total cost calculated.

