#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each of the t test cases, n is an integer such that 1 ≤ n ≤ 10, and s is a string of length n consisting of the characters 'W' and 'B', with at least one 'B' in s.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4; n is an integer such that 1 ≤ n ≤ 10; s is a new input string consisting of the characters 'W' and 'B', with at least one 'B' in s; ma is 0; mi is the position of the first 'B' in s; m is an input integer; c is the position of the first 'B' in s; d is 0; l is an empty list.
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4; n is an integer such that 1 ≤ n ≤ 10; s is a new input string consisting of the characters 'W' and 'B', with at least one 'B' in s; ma is the position of the last 'B' in s; mi is the position of the first 'B' in s; m is an input integer; c is the position of the first 'B' in s; d is 0; l is an empty list.
    return ma - mi + 2
    #The program returns the difference between the position of the last 'B' and the first 'B' in the string `s`, plus 2.
#Overall this is what the function does:The function reads an integer `m` and a string `s` consisting of 'W' and 'B' characters, with at least one 'B'. It calculates and returns the difference between the position of the last 'B' and the first 'B' in the string `s`, plus 2.

