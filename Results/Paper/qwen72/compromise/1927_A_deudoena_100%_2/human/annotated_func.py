#State of the program right berfore the function call: The function should take two parameters: an integer t (1 \le t \le 10^4) representing the number of test cases, and a list of tuples test_cases, where each tuple contains an integer n (1 \le n \le 10) and a string s of length n consisting of characters 'W' or 'B'. Each string s is guaranteed to have at least one 'B'.
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
        
    #State: `c` is the position of the first 'B' in `s`, `d` is 0, `ma` is 0, `mi` is the position of the first 'B' in `s`, `m` is the input integer, `s` is the input string, `t` is an integer between 1 and 10^4, `test_cases` is a list of tuples where each tuple contains an integer between 1 and 10 and a string of that length consisting of characters 'W' or 'B' with at least one 'B', `l` is an empty list.
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: `c` is the position of the first 'B' in `s`, `d` is the distance from the end of `s` to the last 'B' in `s` plus 1, `ma` is the position of the last 'B' in `s`, `mi` is the position of the first 'B' in `s`, `m` is the input integer, `s` is the input string, `t` is an integer between 1 and 10^4, `test_cases` is a list of tuples where each tuple contains an integer between 1 and 10 and a string of that length consisting of characters 'W' or 'B' with at least one 'B', `l` is an empty list.
    return ma - mi + 2
    #The program returns the difference between the position of the last 'B' in `s` (`ma`) and the position of the first 'B' in `s` (`mi`), plus 2.
#Overall this is what the function does:The function `func_1` reads an integer `m` and a string `s` from the input. It then calculates the positions of the first and last occurrences of the character 'B' in the string `s`. The function returns the difference between the position of the last 'B' and the position of the first 'B', plus 2. The function does not use the parameters `t` and `test_cases` mentioned in the comments.

