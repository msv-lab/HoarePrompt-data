#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 10, and s is a string of length n consisting of characters 'W' or 'B', with at least one 'B' in the string.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is an integer such that 1 <= n <= 10; `s` is a string of length `n` consisting of characters 'W' or 'B', with at least one 'B' in the string; `ma` is 0; `mi` is the position of the first 'B' in the string `s`; `m` is an input integer; `c` is the position of the first 'B' in the string `s`; `d` is 0; `l` is an empty list.
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is an integer such that 1 <= n <= 10; `s` is a string of length `n` consisting of characters 'W' or 'B', with at least one 'B' in the string; `ma` is the position of the last 'B' in the string `s` when counting from the start of the string; `mi` is the position of the first 'B' in the string `s`; `m` is an input integer; `c` is the position of the first 'B' in the string `s`; `d` is the number of characters from the end of the string to the last 'B'; `l` is an empty list.
    return ma - mi + 2
    #The program returns the difference between the position of the last 'B' (ma) and the position of the first 'B' (mi) in the string `s`, plus 2.
#Overall this is what the function does:The function calculates and returns the length of the substring of `s` that starts at the first occurrence of 'B' and ends at the last occurrence of 'B', inclusive, plus 2.

