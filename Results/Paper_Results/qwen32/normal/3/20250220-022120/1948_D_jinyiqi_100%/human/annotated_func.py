#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each of the t test cases, s is a string consisting of lowercase Latin letters and/or question marks, with 1 <= |s| <= 5000. The total length of all strings s over all test cases does not exceed 5000.
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
        
    #State: The program completes without printing anything.
    print(0)
    #This is printed: 0
#Overall this is what the function does:The function reads a string `s` from the input, checks for specific patterns within the string, and prints the length of the longest palindromic substring that can be formed by replacing question marks with matching characters. If no such substring is found, it prints 0. The function does not return any value.

