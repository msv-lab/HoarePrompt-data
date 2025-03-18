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
        
    #State: Output State: The function has executed all its iterations without printing any value and returned None. This means that within the loop, the condition `count == j` was never met for any value of `k` in the range from 0 to `n - j - 1` for all iterations of `j` from `n // 2` down to 1. Therefore, the function did not find any sequence where `count` reached the value of `j` and thus returned None after completing all iterations.
    print(0)
    #This is printed: 0
#Overall this is what the function does:The function processes a string `s` consisting of lowercase Latin letters and/or question marks. It checks for sequences within the string where characters match or are question marks, up to a certain length defined by half the string's length. If such a sequence is found, it prints twice the length of the sequence and returns. If no such sequence exists, it prints `0`. The function does not return any value explicitly.

