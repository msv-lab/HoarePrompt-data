#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each testcase, s is a string consisting of lowercase Latin letters and/or question marks such that 1 ≤ |s| ≤ 5000. The total length of all strings s over all testcases does not exceed 5000.
def func_1():
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
        
    #State: The loop has completed all its iterations, and no print statement was executed. Therefore, no output was generated.
    return 0
    #The program returns 0
#Overall this is what the function does:The function processes a string `s` and an integer `n`. It iterates through possible substrings of `s` to find pairs of characters that match or are replaced by '?'. If it finds a valid pair of length `j`, it prints `2 * j` and returns immediately. If no such pair is found after checking all possible lengths, it returns 0.

