#State of the program right berfore the function call: The function should take two parameters: an integer `t` (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of tuples `test_cases` where each tuple contains an integer `n` (1 ≤ n ≤ 10) and a string `s` of length `n` consisting of 'W' and 'B' characters, with at least one 'B' in each string.
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
        
    #State: `t` is an integer (1 ≤ t ≤ 10^4), `test_cases` is a list of tuples where each tuple contains an integer `n` (1 ≤ n ≤ 10) and a string `s` of length `n` consisting of 'W' and 'B' characters, with at least one 'B' in each string, `ma` is 0, `mi` is the position of the first 'B' character in `s` (1-indexed), `m` is an input integer, `s` is a non-empty string, `c` is the position of the first 'B' character in `s` (1-indexed), `d` is 0, `l` is an empty list.
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: `t` is an integer (1 ≤ t ≤ 10^4), `test_cases` is a list of tuples where each tuple contains an integer `n` (1 ≤ n ≤ 10) and a string `s` of length `n` consisting of 'W' and 'B' characters, with at least one 'B' in each string, `ma` is the position of the last 'B' character in `s` (1-indexed), `mi` is the position of the first 'B' character in `s` (1-indexed), `m` is an input integer, `s` is a non-empty string, `c` is the position of the first 'B' character in `s` (1-indexed), `d` is the position of the last 'B' character in `s` (1-indexed), `l` is an empty list.
    return ma - mi + 2
    #The program returns the difference between the position of the last 'B' character and the position of the first 'B' character in the string `s` (both 1-indexed), plus 2.
#Overall this is what the function does:The function `func_1` reads an integer `m` and a string `s` from user input. It then calculates and returns the difference between the position of the last 'B' character and the position of the first 'B' character in the string `s` (both 1-indexed), plus 2. The function does not use the parameters `t` and `test_cases` as described in the annotations.

