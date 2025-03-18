#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each testcase, s is a string consisting of lowercase Latin letters and/or question marks such that 1 ≤ |s| ≤ 5000. The total length of all strings s does not exceed 5000.
def func_1():
    s = list(input())
    n = len(s)
    for j in range(n // 2, 0, -1):
        count = 0
        
        for k in range(0, n - j):
            if s[k] == '?' or s[k + j] == '?' or s[k] == s[k + j]:
                count += 1
            else:
                count = 0
            if count == j:
                print(count * 2)
                return
        
    #State: Output State: The value printed is the maximum count * 2 where count is the length of the longest substring that matches the condition: each character in the substring either matches the corresponding character in the mirrored position or is a question mark (?). If no such substring exists, nothing is printed.
    print(0)
    #This is printed: 0
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase Latin letters and/or question marks. It searches for the longest substring within `s` where each character either matches the corresponding character in the mirrored position or is a question mark. If such a substring exists, it prints twice the length of this substring; otherwise, it prints 0.

