#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 10, and s is a string of length n consisting of characters 'W' and 'B', where at least one character is 'B'.
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
        
    #State: Output State: `ma` is 0, `mi` is the position of the first 'B' in the string `s`, `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 10, `s` is a string of length n consisting of characters 'W' and 'B', where at least one character is 'B', `m` is an input integer, `c` is the length of the substring of `s` up to and including the first 'B', `d` is 0, `l` is an empty list.
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: `ma` is the distance from the end of the string `s` to the first 'B', `mi` is the position of the first 'B' in the string `s`, `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 10, `s` is a string of length n consisting of characters 'W' and 'B', where at least one character is 'B', `m` is an input integer, `c` is the length of the substring of `s` up to and including the first 'B', `d` is 0, `l` is an empty list.
    return ma - mi + 2
    #The program returns the distance from the end of the string `s` to the first 'B' minus the position of the first 'B' in the string `s` plus 2.
#Overall this is what the function does:The function processes a string `s` containing characters 'W' and 'B', and an integer `t`. It calculates and returns the distance from the end of the string `s` to the first occurrence of 'B', subtracts the position of the first 'B' in the string `s`, and adds 2 to the result.

