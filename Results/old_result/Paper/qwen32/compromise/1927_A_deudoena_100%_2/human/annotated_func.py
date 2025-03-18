#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 10, and s is a string of length n consisting of characters 'W' and 'B', with at least one 'B' in s.
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
        
    #State: t is an integer such that 1 <= t <= 10^4; n is an integer such that 1 <= n <= 10; s is the string input by the user consisting of characters 'W' and 'B', with at least one 'B' in s; ma is 0; mi is the position (1-based index) of the first 'B' in s; m is the integer input by the user; c is the position (1-based index) of the first 'B' in s; d is 0; l is an empty list.
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: - `t` remains the same.
    #- `n` remains the same.
    #- `s` remains the same.
    #- `ma` is set to the position of the first 'B' from the start of the string when iterating from the end.
    #- `mi` remains the same.
    #- `m` remains the same.
    #- `c` remains the same.
    #- `d` is the position of the first 'B' from the end of the string.
    #- `l` remains the same.
    #
    #In simpler terms, `ma` will now hold the 0-based index of the first 'B' from the start of the string when counted from the end, and `d` will hold the 1-based index of this 'B' from the end of the string.
    #
    #Output State:
    return ma - mi + 2
    #The program returns ma - mi + 2, where ma is the 0-based index of the first 'B' from the start of the string when counted from the end, and mi is the given value of mi.
#Overall this is what the function does:The function calculates and returns the difference between the 0-based index of the first 'B' from the end of the string and the 0-based index of the first 'B' from the start of the string, then adds 2 to this difference. It processes a string `s` of length `n` consisting of 'W' and 'B' characters, with at least one 'B' present.

