#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, there is an integer n (1 ≤ n ≤ 10) representing the length of the strip, followed by a string s of length n consisting of characters 'W' and 'B', where 'W' denotes a white cell and 'B' denotes a black cell. It is guaranteed that at least one cell in each strip is black.
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
        
    #State: t is an integer (1 ≤ t ≤ 10^4), n is an integer (1 ≤ n ≤ 10), s is a string of length n consisting of 'W' and 'B' with at least one 'B', ma is 0, mi is the 1-based index of the first 'B' in s, m is the number of test cases, c is the 1-based index of the first 'B' in s, d is 0, and l is an empty list.
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: - `t` remains the same.
    #- `n` remains the same.
    #- `s` remains the same.
    #- `ma` is set to the 1-based index of the first 'B' from the start of the string.
    #- `mi` remains the same.
    #- `m` remains the same.
    #- `c` remains the same.
    #- `d` is equal to `k`, the number of iterations the loop executed.
    #- `l` remains an empty list.
    #
    #In natural language, after the loop has executed all necessary iterations, the variable `ma` will hold the 1-based index of the first 'B' from the start of the string `s`, and `d` will reflect how many characters from the end of the string were checked before finding the first 'B'. All other variables remain unchanged.
    #
    #Output State:
    return ma - mi + 2
    #The program returns the value of `ma - mi + 2`, where `ma` is the 1-based index of the first 'B' from the start of the string `s`, and `mi` remains unchanged.
#Overall this is what the function does:The function calculates and returns the number of cells between the first and last black cells ('B') in a given string `s` of length `n`, inclusive, plus two. The string `s` consists of 'W' (white) and 'B' (black) cells, and it is guaranteed to contain at least one 'B'.

