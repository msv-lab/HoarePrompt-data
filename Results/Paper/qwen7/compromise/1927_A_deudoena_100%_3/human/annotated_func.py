#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 10, and s is a string consisting of n characters where each character is either 'W' (white) or 'B' (black), with at least one 'B' in the string.
def func_1():
    ma = mi = 0
    m = int(input())
    s = input()
    c = d = 0
    l = []
    for j in s:
        c += 1
        
        if j == 'B':
            mi = c
            break
        
    #State: Output State: `ma` is 0, `mi` is 0, `m` is an input integer, `s` is an input string, `c` is the length of the string `s`, `d` is 0, `l` is an empty list.
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: Output State: `ma` is the length of the string `s` minus the position of the first 'B' from the end, `mi` is 0, `m` is an input integer, `s` is an input string, `c` is the length of the string `s`, `d` is the number of characters in `s`, `l` is an empty list.
    return ma - mi + 2
    #The program returns the length of the string `s` minus the position of the first 'B' from the end, plus 2.
#Overall this is what the function does:The function processes a binary string `s` (consisting of 'W' and 'B') and calculates a value based on the positions of the first 'B' from the start and the end of the string. Specifically, it returns the length of the string minus the position of the first 'B' from the end, plus 2. This value is returned without any parameters being passed directly to the function.

