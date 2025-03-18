#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 10 and s is a string of length n consisting of characters 'W' and 'B', where at least one character in s is 'B'.
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
        
    #State: The output state after the loop executes all the iterations is as follows: `s` is a string of length `n` consisting of characters 'W' and 'B', with at least one character being 'B'; `j` is the last character in the string `s`; `c` is equal to `n`; `mi` is the index (1-based) of the first 'B' in the string `s`, or 0 if there is no 'B' in the string. The variable `d` is 0, `l` is an empty list, and the other variables (`ma`, `t`, `n`, `m`) retain their initial values.
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: Postcondition: `s` is a string of length `n` consisting of characters 'W' and 'B', with at least one character being 'B'; `j` is the last character in the original string `s`; `c` is `n`; `mi` is the index (1-based) of the first 'B' in the string `s`, or 0 if there is no 'B' in the string `s`; `d` is `n`; `l` is an empty list; `ma` is `0`.
    return ma - mi + 2
    #The program returns a value which is the result of subtracting the index of the first 'B' (or 0 if no 'B' exists) from 'ma' (which is 0), and then adding 2.
#Overall this is what the function does:The function processes a binary string `s` of length `n` (where 1 ≤ n ≤ 10) consisting of characters 'W' and 'B'. It calculates and returns a value based on the positions of the first and last 'B' characters in the string. Specifically, it returns the difference between the position of the last 'B' and the first 'B', plus 2. If no 'B' is found, it returns 2.

