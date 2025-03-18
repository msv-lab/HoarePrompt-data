#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, s is a string consisting of lowercase Latin letters and/or question marks, with 1 <= |s| <= 5000. The total length of all strings s over all testcases does not exceed 5000.
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
        
    #State: The function either prints a value of the form `2 * j` and terminates, or it does not print anything if no such sequence is found.
    print(0)
    #This is printed: 0
#Overall this is what the function does:The function `func_1` reads a string `s` consisting of lowercase Latin letters and/or question marks, and determines the longest even-length palindromic substring that can be formed by replacing question marks with appropriate characters. If such a substring exists, it prints its length; otherwise, it prints `0`.

