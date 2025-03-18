#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of tuples, where each tuple contains an integer n (1 ≤ n ≤ 10) and a string s of length n consisting of 'W' or 'B' characters, with at least one 'B' in each string.
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
        
    #State: `c` is the position of the first 'B' in `s` or the length of `s` if 'B' is not found, `d` is 0, `ma` is 0, `mi` is the position of the first 'B' in `s` or 0 if 'B' is not found, `m` is an input integer, `s` is an input string, `t` is an integer (1 ≤ t ≤ 10^4), the list of tuples is unchanged, `l` is an empty list.
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: `c` is the position of the first 'B' in `s` or the length of `s` if 'B' is not found, `d` is the position of the last 'B' in `s` from the end of the string plus 1, `ma` is the position of the last 'B' in `s` from the end of the string, `mi` is the position of the first 'B' in `s` or 0 if 'B' is not found, `m` is an input integer, `s` is a non-empty input string, `t` is an integer (1 ≤ t ≤ 10^4), the list of tuples is unchanged, `l` is an empty list.
    return ma - mi + 2
    #The program returns the difference between the position of the last 'B' in `s` from the end of the string (`ma`) and the position of the first 'B' in `s` (`mi`), plus 2. If 'B' is not found in `s`, `mi` is 0, and the program returns `ma + 2`.
#Overall this is what the function does:The function `func_1` takes no parameters and does not return any value as specified in the annotated code. However, it reads an integer `m` and a string `s` from the user input. It calculates the position of the first occurrence of 'B' in `s` (`mi`) and the position of the last occurrence of 'B' in `s` from the end of the string (`ma`). The function returns the difference between these positions plus 2. If 'B' is not found in `s`, `mi` is 0, and the function returns `ma + 2`. The function does not modify any external state or parameters.

