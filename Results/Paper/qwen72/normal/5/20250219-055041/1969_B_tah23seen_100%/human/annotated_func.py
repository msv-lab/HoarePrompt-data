#State of the program right berfore the function call: s is a binary string (2 ≤ |s| ≤ 2 · 10^5; s_i ∈ {0, 1}) — the string you need to sort.
def func_1(s):
    cost = 0
    one = 0
    for i in s:
        if i == '1':
            one += 1
        elif i == '0' and one > 0:
            cost += one + 1
        
    #State: `s` is a binary string (2 ≤ |s| ≤ 2 · 10^5; s_i ∈ {0, 1}), `cost` is the total cost accumulated based on the loop logic, and `one` is the count of consecutive '1's at the end of the string.
    return cost
    #The program returns the total cost accumulated based on the loop logic.
#Overall this is what the function does:The function `func_1` accepts a binary string `s` and returns an integer `cost`. The `cost` is calculated by iterating through the string `s` and for each '0' encountered after at least one '1', the cost is incremented by the number of '1's seen so far plus one. The final state of the program is that `s` remains unchanged, and `cost` represents the total accumulated cost based on the specified logic.

