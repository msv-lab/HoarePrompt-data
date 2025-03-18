#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each testcase, s is a string consisting of lowercase Latin letters and/or question marks such that 1 ≤ |s| ≤ 5000. The total length of all strings s over all testcases does not exceed 5000.
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
        
    #State: Output State: The output state will be the value printed inside the loop if there exists a pair of indices (k, k+j) in the list `s` such that `s[k] == s[k + j]` or `s[k] == '?'` or `s[k + j] == '?',` and the count of such pairs equals `j`. If no such pair is found for any `j`, the output state will be nothing (i.e., no output).
    print(0)
    #This is printed: 0
#Overall this is what the function does:The function processes a string `s` consisting of lowercase Latin letters and/or question marks. It checks for pairs of indices `(k, k+j)` in the string where either the characters at these indices are equal or one of them is a question mark. If such pairs exist and their count equals `j`, it prints `2*j` and returns immediately. If no valid pairs are found for any `j` from half the length of the string down to 1, it prints `0`. The function does not return anything explicitly but outputs a value based on the conditions met within the string.

