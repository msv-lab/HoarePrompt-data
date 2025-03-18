#State of the program right berfore the function call: s is a binary string (a string consisting of only '0's and '1's) with a length of at least 2.
def func_1(s):
    cost = 0
    one = 0
    for i in s:
        if i == '1':
            one += 1
        elif i == '0' and one > 0:
            cost += one + 1
        
    #State: `s` is unchanged, `one` is the count of consecutive '1's at the end of `s` not followed by a '0', and `cost` is the sum of `one + 1` for every sequence of consecutive '1's followed by a '0' in `s`.
    return cost
    #The program returns the sum of `one + 1` for every sequence of consecutive '1's followed by a '0' in the string `s`.
#Overall this is what the function does:The function accepts a binary string `s` and returns the sum of `one + 1` for every sequence of consecutive '1's that is immediately followed by a '0'.

