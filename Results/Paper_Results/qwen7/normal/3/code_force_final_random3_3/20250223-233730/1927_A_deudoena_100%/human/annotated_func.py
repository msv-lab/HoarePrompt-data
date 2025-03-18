#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 10, and s is a string of length n consisting of characters 'W' and 'B', where at least one character is 'B'.
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
        
    #State: Output State: `ma` is 0, `mi` is the length of the string `s`, `m` is an input integer, `s` is a non-empty string starting with 'B', `c` is the length of the string `s`, `d` is 0, `l` is an empty list, and `j` is the last character of `s`.
    #
    #Explanation: The loop continues to increment `c` and check if the current character `j` is 'B'. Since the loop breaks as soon as it encounters the first 'B', `c` will eventually reach the length of the string `s`. The value of `mi` will be set to the position (index + 1) of the first 'B' encountered, or the length of the string if no 'B' is found. All other variables remain unchanged as they are not affected by the loop.
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: `ma` is the length of the string `s` - `d`, `mi` is the length of the string `s`, `m` is an input integer, `s` is a non-empty string starting with 'B', `c` is the length of the string `s`, the current value of `j` is the last character of the original string `s`, `d` is equal to the length of the string `s`, `l` is an empty list, and the program breaks out of the most internal loop or if statement.
    return ma - mi + 2
    #The program returns the difference between the length of string `s` minus `d` and the length of string `s`, plus 2.
#Overall this is what the function does:The function processes a string `s` containing characters 'W' and 'B', where at least one character is 'B'. It calculates and returns the difference between the length of the string `s` minus the distance from the end of the string to the first occurrence of 'B', plus 2.

