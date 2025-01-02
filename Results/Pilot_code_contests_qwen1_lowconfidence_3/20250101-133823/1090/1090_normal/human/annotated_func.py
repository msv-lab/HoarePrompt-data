#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10³, s is a string of length n consisting of lowercase English letters, and a1, a2, ..., a26 are 26 integers such that 1 ≤ ai ≤ 10³.
def func():
    n = input()
    str = raw_input()
    arr = raw_input().split()
    arr = map(eval, arr)
    MOD = 1000000000.0 + 7
    dp = [0] * 3200
    dp[0] = 1
    lastMatch = [0] * 3200
    for i in range(len(lastMatch)):
        lastMatch[i] = i
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 10^3\), `s` is a string of length `n` consisting of lowercase English letters, `str` is a string (the input from the user), `arr` is a list of evaluated expressions, `MOD` is `1000000007.0`, `dp` is a list of 3200 elements where the first element is 1 and the rest are 0, `lastMatch` is a list of 3200 elements where each element is its index `i`, and `len(lastMatch)` is 3200.
    maxSubLen = 0
    for i in range(1, len(str) + 1):
        j = 1
        
        k = arr[ord(str[i - 1]) - ord('a')]
        
        while j <= k and i - j >= 0:
            maxSubLen = max(j, maxSubLen)
            dp[i] = (dp[i] + dp[i - j]) % MOD
            t = i - j - 1
            lastMatch[t + 1] = max(lastMatch[t + 1], i - 1)
            t = t if t > 0 else 0
            k = min(k, arr[ord(str[t]) - ord('a')])
            j += 1
        
    #State of the program after the  for loop has been executed: `dp[i]` is the final value calculated by the loop operations, `j` is `i + 1`, `k` is the minimum value it was updated to during the loop iterations, `maxSubLen` is the maximum value of `j` during the loop iterations, `t` is `0` if `i - j - 1` is 0 or less, otherwise `t` is `i - j - 1`, `lastMatch` contains the maximum values it was updated to during the loop iterations, `arr`, `MOD`, `n`, `s`, `str`, `len(lastMatch)`, `maxSubLen`, and `dp[0]` remain unchanged.
    lastIndex = 0
    lastStrIndex = len(str) - 1
    subNum = 0
    while lastIndex != lastStrIndex:
        subNum += 1
        
        if lastIndex == lastMatch[lastIndex]:
            lastIndex += 1
        else:
            lastIndex = lastMatch[lastIndex]
        
    #State of the program after the loop has been executed: `dp[i]` is the final value calculated by the loop operations, `j` is `i + 1`, `k` is the minimum value it was updated to during the loop iterations, `maxSubLen` is the maximum value of `j` during the loop iterations, `t` is `0` if `i - j - 1` is 0 or less, otherwise `t` is `i - j - 1`, `lastMatch` contains the maximum values it was updated to during the loop iterations, `arr`, `MOD`, `n`, `s`, `str`, `lastStrIndex` is `len(str) - 1`, `maxSubLen`, `dp[0]`, and `lastIndex` is `lastStrIndex`, `subNum` is the total number of iterations the loop has executed.
    print(dp[len(str)], maxSubLen, subNum, sep='\n')
#Overall this is what the function does:The function processes a string `s` of length `n` and a list of integers `arr` representing lengths, to compute three values: the number of distinct substrings that can be formed based on the given lengths, the maximum length of a substring that meets a specific condition, and the number of operations required to achieve these results. Specifically, the function calculates:

1. `dp[len(str)]`: The number of distinct substrings of `s` that can be formed under certain conditions.
2. `maxSubLen`: The maximum length of a valid substring found during the computation.
3. `subNum`: The number of operations performed to determine the valid substrings.

The function reads the string `s` and a list of integers `arr` from the standard input. It then iterates through the string to update a dynamic programming array `dp` and a list `lastMatch` to track the last occurrence of valid substrings. After processing the string, it counts the number of distinct substrings and prints the results.

