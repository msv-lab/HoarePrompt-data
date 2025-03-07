#State of the program right berfore the function call: s is a binary string (2 ≤ |s| ≤ 2 · 10^5; s_i ∈ {0, 1}) — the string you need to sort.
def func_1(s):
    cost = 0
    one = 0
    for i in s:
        if i == '1':
            one += 1
        elif i == '0' and one > 0:
            cost += one + 1
        
    #State: Output State: `s` is a binary string (unchanged), `cost` is the total cost calculated based on the number of '0's following '1's in the string, `one` is the count of '1's in the string.
    return cost
    #The program returns the total cost calculated based on the number of '0's following '1's in the binary string `s`.
#Overall this is what the function does:The function `func_1` accepts a binary string `s` and returns an integer `cost` representing the total cost calculated based on the number of '0's that follow '1's in the string. The string `s` remains unchanged after the function call. The cost is incremented by the count of '1's plus one for each '0' that follows a '1' in the string.

