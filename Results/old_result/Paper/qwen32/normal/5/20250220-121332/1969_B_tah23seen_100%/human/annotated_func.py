#State of the program right berfore the function call: s is a binary string (a string consisting of only '0's and '1's) with length 2 ≤ |s| ≤ 2 · 10^5.
def func_1(s):
    cost = 0
    one = 0
    for i in s:
        if i == '1':
            one += 1
        elif i == '0' and one > 0:
            cost += one + 1
        
    #State: `s` is the original binary string, `one` is the count of consecutive '1's at the end of the string if it ends with '1's, otherwise `one` is 0, and `cost` is the sum of `(number of consecutive '1's + 1)` for each segment of consecutive '1's in the string that is followed by a '0'.
    return cost
    #The program returns the cost, which is the sum of (number of consecutive '1's + 1) for each segment of consecutive '1's in the string that is followed by a '0'.
#Overall this is what the function does:The function accepts a binary string `s` and returns the cost, which is calculated as the sum of (number of consecutive '1's + 1) for each segment of consecutive '1's in the string that is immediately followed by a '0'.

