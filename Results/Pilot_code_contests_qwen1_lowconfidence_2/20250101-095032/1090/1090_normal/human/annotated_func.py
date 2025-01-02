#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^3, s is a string of length n consisting of lowercase English letters, and a1, a2, ..., a26 is a list of 26 integers where 1 ≤ ai ≤ 10^3 for each i.
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
        
    #State of the program after the  for loop has been executed: `a1` is a list of 26 integers where \(1 \leq a_i \leq 10^3\) for each \(i\), `n` is an input integer, `str` is a new input string from the user, `arr` is a map object where each element is the evaluated version of the corresponding string in the original list, `MOD` is 1000000007.0, `dp` is a list of 3200 elements where the first element is 1 and all others are 0, `lastMatch` is a list of 3200 elements where each element is equal to its index, `i` is 3200.
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
        
    #State of the program after the  for loop has been executed: Output State:
    lastIndex = 0
    lastStrIndex = len(str) - 1
    subNum = 0
    while lastIndex != lastStrIndex:
        subNum += 1
        
        if lastIndex == lastMatch[lastIndex]:
            lastIndex += 1
        else:
            lastIndex = lastMatch[lastIndex]
        
    #State of the program after the loop has been executed: `lastIndex` is equal to `lastStrIndex`, `lastStrIndex` is the length of `str` minus 1, and `subNum` is the number of times the loop executed. If `lastIndex` equals `lastMatch[lastIndex]` at any point, it will increment by 1, otherwise it will be updated to `lastMatch[lastIndex]` until it reaches `lastStrIndex`.
    print(dp[len(str)], maxSubLen, subNum, sep='\n')
#Overall this is what the function does:The function `func` accepts three parameters: `n`, `s`, and `a1, a2, ..., a26`. The parameter `n` is an integer such that 1 ≤ n ≤ 10^3, `s` is a string of length `n` consisting of lowercase English letters, and `a1, a2, ..., a26` is a list of 26 integers where 1 ≤ ai ≤ 10^3 for each i. After performing several operations, the function calculates the following:

1. It constructs a dynamic programming array `dp` and a `lastMatch` array.
2. It iterates through the string `s` to compute the maximum substring length (`maxSubLen`) using the values from the `arr` list.
3. It then uses the `dp` and `lastMatch` arrays to count the number of substrings (`subNum`) that can be formed based on certain conditions.
4. Finally, it prints the results of `dp[len(str)]`, `maxSubLen`, and `subNum`.

Potential edge cases and missing functionality:
- The function assumes valid inputs for `n`, `s`, and `a1, a2, ..., a26`, but it does not handle invalid inputs (e.g., `n` outside the range 1 to 10^3, `s` not having length `n`, or `a1, a2, ..., a26` not containing 26 valid integers).
- The function does not modify the input parameters; it treats them as read-only.
- The function's overall goal is not explicitly stated, but it appears to be related to computing some properties of the string `s` based on the given constraints and the values in the `arr` list.

