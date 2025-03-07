#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 10 and s is a string of length n consisting of characters 'W' and 'B', where at least one character is 'B'.
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
        
    #State: The string `s` is a sequence of 'W' and 'B' characters with at least one 'B'. The variable `j` is the last character in `s` that is 'B'. The variable `c` is equal to the length of `s`. The variable `mi` is equal to the index (position) of the first 'B' in `s`.
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: The string `s` is a sequence of 'W' and 'B' characters with at least one 'B'. The variable `j` is the last 'B' in the reversed string `s[::-1]`, the variable `c` is the length of `s`, `mi` is the index of the first 'B' in the original string `s`, and `ma` is equal to `len(s) - d - (number of iterations - 1)`. The variable `d` has been incremented by the total number of iterations of the loop.
    return ma - mi + 2
    #The program returns the difference between the index of the last 'B' in the reversed string and the index of the first 'B' in the original string, plus 2.
#Overall this is what the function does:The function processes a string `s` consisting of characters 'W' and 'B', and calculates the difference between the index of the last 'B' in the reversed string and the index of the first 'B' in the original string, then adds 2 to this difference. The function returns this computed value.

