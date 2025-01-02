#State of the program right berfore the function call: s is a string of length N consisting of 'L' and 'R', and an integer K is a non-negative integer such that 1 <= K <= 10^5.
def func_1(s):
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] == 'L' and i >= 1 and s[i - 1] == 'L':
            ans += 1
        elif s[i] == 'R' and i <= n - 2 and s[i + 1] == 'R':
            ans += 1
        
    #State of the program after the  for loop has been executed: `s` is a string of length `N` consisting of 'L' and 'R', `n` is `N`, `ans` is the count of consecutive 'LL' substrings and consecutive 'RR' substrings in `s`.
    return ans
    #The program returns `ans`, which is the count of consecutive 'LL' and 'RR' substrings in string `s` of length `N`
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of characters 'L' and 'R', and returns the count of consecutive 'LL' and 'RR' substrings in `s`. Specifically, it iterates through the string and increments the count (`ans`) whenever it encounters two consecutive 'L' characters ('LL') or two consecutive 'R' characters ('RR'). The function correctly handles the entire string, including edge cases where the string might start or end with 'LL' or 'RR'. It also properly accounts for overlapping substrings; for example, in the string "LLRLL", both occurrences of 'LL' would be counted separately. The function does not require the parameter `K` mentioned in the initial description, as it is not used within the function.

