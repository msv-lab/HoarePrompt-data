#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n is an integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func_1(s):
    if (s == 'mapie') :
        return 1
        #The program returns 1
    #State: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n is an integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6. Additionally, s is not equal to 'mapie'.
    ans = 0
    while s.find('map') != -1:
        s = s[:s.find('map')] + s[s.find('map') + 2:]
        
        ans += 1
        
    #State: - `t` remains unchanged as it is not affected by the loop.
    #- `n` will be reduced by 2 for each occurrence of `'map'` removed from `s`. Therefore, the new length of `s` will be `n - 2 * (number of 'map' occurrences)`.
    #- `s` will no longer contain the substring `'map'`.
    #- `ans` will be equal to the total number of `'map'` substrings removed from `s`.
    #
    #Thus, the final output state can be described as:
    #
    #Output State:
    while s.find('pie') != -1:
        s = s[:s.find('pie')] + s[s.find('pie') + 2:]
        
        ans += 1
        
    #State: `t` remains unchanged, `n` is reduced by the number of 'pie' substrings removed, `s` does not contain any 'pie' substrings, `ans` is equal to the number of 'pie' substrings removed.
    return ans
    #The program returns the number of 'pie' substrings removed from the string `s`.
#Overall this is what the function does:The function `func_1` accepts a string `s` and returns 1 if `s` is exactly 'mapie'. Otherwise, it returns the number of 'map' and 'pie' substrings removed from `s`.

