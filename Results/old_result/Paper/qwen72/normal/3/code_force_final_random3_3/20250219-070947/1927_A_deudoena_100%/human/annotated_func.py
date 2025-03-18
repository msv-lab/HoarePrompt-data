#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 10, and s is a string of length n consisting of characters 'W' or 'B', with at least one 'B'.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is an integer such that 1 <= n <= 10, `s` is an input string of length `n` consisting of characters 'W' or 'B', with at least one 'B', `ma` is 0, `m` is an input integer, `c` is the position of the first 'B' in `s`, `d` is 0, `l` is an empty list, and `mi` is the position of the first 'B' in `s`.
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is an integer such that 1 <= n <= 10, `s` is an input string of length `n` consisting of characters 'W' or 'B', with at least one 'B', `m` is an input integer, `c` is the position of the first 'B' in `s`, `d` is the position of the last 'B' in `s` from the end, `l` is an empty list, `mi` is the position of the first 'B' in `s`, and `ma` is the position of the last 'B' in `s` from the start.
    return ma - mi + 2
    #The program returns the value of `ma - mi + 2`, where `ma` is the position of the last 'B' in the string `s` from the start, and `mi` is the position of the first 'B' in the string `s`.
#Overall this is what the function does:The function `func_1` takes no parameters and reads two inputs: an integer `m` and a string `s` of length `n` (1 <= n <= 10) consisting of characters 'W' or 'B', with at least one 'B'. It calculates the distance between the first and last occurrence of 'B' in the string `s` and returns this distance plus 2.

