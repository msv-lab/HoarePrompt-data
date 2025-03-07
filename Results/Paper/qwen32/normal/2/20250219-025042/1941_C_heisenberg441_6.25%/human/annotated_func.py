#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, each test case consists of an integer n such that 1 ≤ n ≤ 10^6, and a string s of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func_1(s):
    if (s == 'mapie') :
        return 1
        #The program returns 1
    #State: t is an integer such that 1 ≤ t ≤ 10^4, each test case consists of an integer n such that 1 ≤ n ≤ 10^6, and a string s of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6. Additionally, the string s is not equal to 'mapie'.
    ans = 0
    while s.find('map') != -1:
        s = s[:s.find('map')] + s[s.find('map') + 2:]
        
        ans += 1
        
    #State: `t` is an integer such that \(1 \leq t \leq 10^4\); `n` is an integer such that \(1 \leq n \leq 10^6\); `s` is a string of length `n - 2 * k` that no longer contains the substring `'map'`, where `k` is the total number of times the substring `'map'` was found and removed; `ans` is `k`.
    while s.find('pie') != -1:
        s = s[:s.find('pie')] + s[s.find('pie') + 2:]
        
        ans += 1
        
    #State: `t` is an integer such that \(1 \leq t \leq 10^4\); `n` is an integer such that \(1 \leq n \leq 10^6\); `s` is a string of length `n - 2 * k - 2 * m` that no longer contains the substring `'map'` or `'pie'`; `ans` is `k + m`.
    return ans
    #The program returns the value of `ans`, which is `k + m`.
#Overall this is what the function does:The function `func_1` accepts a string `s` of lowercase Latin letters. If the string `s` is exactly `'mapie'`, the function returns 1. Otherwise, it removes all occurrences of the substrings `'map'` and `'pie'` from `s`, counting each removal, and returns the total count of these removals.

