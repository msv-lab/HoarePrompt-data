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
        
    #State: The loop has executed all its iterations, and the final value of `count` is either equal to `n - j` (if the condition `count == j` was met at least once during the loop's execution) or 0 (if the condition `count == j` was never met). The variable `k` will be equal to `n - j - 1`, as it increments with each iteration of the loop. The variable `n` remains greater than `j`, and the characters at indices `k` and `k + j` in string `s` continue to meet the specified conditions throughout the loop's execution. If `count` equals `j` at any point, the function prints `count * 2` and returns, thus terminating the loop prematurely.
    return 0
    #The program returns 0
#Overall this is what the function does:The function processes a string `s` and an integer `t` (though `t` is not used in the function), checking for pairs of characters in `s` that are either equal or both question marks. If it finds a sequence where `count` (the number of matching pairs found consecutively) equals the current value of `j` (which decreases from `n//2` to 1), it prints `count * 2` and returns. If no such sequence is found after checking all possible pairs, the function returns 0. The function can return None in cases where the return statement is not explicitly included.

