#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, there are two lines: the first line contains an integer n (1 ≤ n ≤ 10) representing the length of the strip, and the second line contains a string s of length n, consisting of characters 'W' or 'B' where 'W' denotes a white cell and 'B' denotes a black cell. It is guaranteed that there is at least one 'B' in the string s.
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
        
    #State: `ma` is 0, `mi` is the position of the first 'B' in the string `s` (1-indexed), `m` is unchanged, `s` is unchanged, `c` is the position of the first 'B' in the string `s` (1-indexed), `d` is 0, and `l` is an empty list.
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: ma is the 0-indexed position of the last 'B' in s, mi is unchanged, m is unchanged, s is unchanged, c is unchanged, d is the distance from the end of the string to the last 'B', l is an empty list.
    return ma - mi + 2
    #The program returns `ma - mi + 2`, where `ma` is the 0-indexed position of the last 'B' in the string `s`, and `mi` is unchanged.
#Overall this is what the function does:The function calculates and returns the length of the substring in `s` that starts from the first occurrence of 'B' and ends at the last occurrence of 'B', inclusive.

