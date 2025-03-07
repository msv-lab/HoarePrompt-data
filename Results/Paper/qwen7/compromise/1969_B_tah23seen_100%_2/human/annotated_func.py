#State of the program right berfore the function call: s is a binary string (a string consisting of only '0's and/or '1's) with a length between 2 and 200000.
def func_1(s):
    cost = 0
    one = 0
    for i in s:
        if i == '1':
            one += 1
        elif i == '0' and one > 0:
            cost += one + 1
        
    #State: Output State: `s` is a binary string, `one` is the number of '1's in the string `s`, `cost` is the sum of `(number of '1's before each '0') + 1` for every '0' in the string `s`.
    return cost
    #The program returns the sum of (number of '1's before each '0') + 1 for every '0' in the binary string 's'
#Overall this is what the function does:The function accepts a binary string `s` and calculates the sum of (number of '1's before each '0') + 1 for every '0' in the string `s`. It iterates through each character in the string, counting the number of '1's before each '0' and adding this count plus one to the total cost. Finally, it returns the total cost.

