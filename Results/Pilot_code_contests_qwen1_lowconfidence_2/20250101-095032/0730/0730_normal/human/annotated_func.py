#State of the program right berfore the function call: s is a string of length N consisting of characters 'L' and 'R', and 1 <= N <= 10^5. Additionally, K is an integer such that 1 <= K <= 10^5.
def func_1(s):
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] == 'L' and i >= 1 and s[i - 1] == 'L':
            ans += 1
        elif s[i] == 'R' and i <= n - 2 and s[i + 1] == 'R':
            ans += 1
        
    #State of the program after the  for loop has been executed: `s` is a string of length `N` consisting of characters 'L' and 'R', `n` is `N`, `ans` is the count of consecutive 'LL' substrings and consecutive 'RR' substrings in `s`.
    return ans
    #The program returns `ans`, which is the count of consecutive 'LL' and 'RR' substrings in string `s`
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of characters 'L' and 'R' and returns the count of consecutive 'LL' and 'RR' substrings in `s`. It iterates through the string `s` and increments the counter `ans` whenever it finds two consecutive 'L' or two consecutive 'R'. The function handles edge cases where the string might start or end with 'L' or 'R' without causing out-of-range errors by ensuring the indices used for checking consecutive characters are within bounds.

