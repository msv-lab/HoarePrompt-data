#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, s is a string of length between 1 and 5000, consisting only of lowercase Latin letters and/or question marks. The total length of all strings s across all test cases does not exceed 5000.
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
        
    #State: No output printed, function returns without modifying external variables.
    print(0)
    #This is printed: 0
#Overall this is what the function does:The function `func_1` reads a string `s` from input, processes it to find the longest palindromic subsequence that can be formed by replacing question marks with any lowercase Latin letter or leaving them as they are, and prints twice the length of this subsequence if found. If no such subsequence of length greater than 1 is found, it prints 0. This process is repeated for `t` test cases, where `t` is the number of test cases provided as input.

