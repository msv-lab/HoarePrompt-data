#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func_1(s):
    if (s == 'mapie') :
        return 1
        #The program returns 1
    #State: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6. The string s is not equal to 'mapie'.
    ans = 0
    while s.find('map') != -1:
        s = s[:s.find('map')] + s[s.find('map') + 2:]
        
        ans += 1
        
    #State: `s` will be a string with all occurrences of 'map' removed, and `ans` will be the count of how many times 'map' was found and removed.
    while s.find('pie') != -1:
        s = s[:s.find('pie')] + s[s.find('pie') + 2:]
        
        ans += 1
        
    #State: - `s` will be the string with all occurrences of 'pie' removed.
    #- `ans` will be the count of how many times 'pie' was found and removed.
    #
    #Output State:
    return ans
    #The program returns the count of how many times 'pie' was found and removed from the string `s`.
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of lowercase Latin letters. It returns 1 if the string `s` is exactly 'mapie'. Otherwise, it returns the count of how many times the substrings 'map' and 'pie' were found and removed from the string `s`.

