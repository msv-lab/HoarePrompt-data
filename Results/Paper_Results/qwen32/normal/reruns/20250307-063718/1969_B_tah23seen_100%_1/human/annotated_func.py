#State of the program right berfore the function call: s is a binary string (a string consisting of only '0's and '1's) with a length between 2 and 2 * 10^5.
def func_1(s):
    cost = 0
    one = 0
    for i in s:
        if i == '1':
            one += 1
        elif i == '0' and one > 0:
            cost += one + 1
        
    #State: `cost` is the accumulated cost based on the occurrences of '0's and preceding counts of '1's, and `one` is the count of trailing '1's in `s`.
    return cost
    #The program returns `cost`, which is the accumulated cost based on the occurrences of '0's and preceding counts of '1's in the string `s`.
#Overall this is what the function does:The function accepts a binary string `s` and calculates an accumulated cost based on the occurrences of '0's and the preceding counts of '1's in the string. It returns this accumulated cost.

