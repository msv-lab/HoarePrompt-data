#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each of the t test cases, n is an integer such that 1 <= n <= 10, and s is a string of length n consisting of characters 'W' and 'B' with at least one 'B' present.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is an integer such that 1 <= n <= 10; `s` is a new input string of length n consisting of characters 'W' and 'B' with at least one 'B' present; `ma` is 0; `mi` is k if the first 'B' is at position k; `m` is an input integer; `c` is k; `d` is 0; `l` is an empty list.
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is an integer such that 1 <= n <= 10; `s` is a new input string of length `n` consisting of characters 'W' and 'B' with at least one 'B' present; `ma` is the position of the last 'B' in the original string `s`; `mi` is k if the first 'B' is at position k; `m` is an input integer; `c` is k; `d` is the number of characters processed until the first 'B' is encountered in the reversed string; `l` is an empty list; `j` is 'B'.
    return ma - mi + 2
    #The program returns the difference between the position of the last 'B' (ma) and the position of the first 'B' (mi) in the string `s`, plus 2.
#Overall this is what the function does:The function calculates and returns the difference between the position of the last 'B' and the position of the first 'B' in a given string `s`, plus 2. The string `s` consists of characters 'W' and 'B' with at least one 'B' present.

