#State of the program right berfore the function call: s is a binary string (a string consisting of only '0's and '1's) with a length of at least 2.
def func_1(s):
    cost = 0
    one = 0
    for i in s:
        if i == '1':
            one += 1
        elif i == '0' and one > 0:
            cost += one + 1
        
    #State: s is a binary string with a length of at least 2; cost is the total calculated cost based on the pattern of '0's following '1's; one is 0.
    return cost
    #The program returns the total calculated cost based on the pattern of '0's following '1's in the binary string `s`.
#Overall this is what the function does:The function calculates and returns the total cost based on the pattern of '0's following '1's in a given binary string `s`.

