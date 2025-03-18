#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters, and its length n satisfies 1 ≤ n ≤ 10^6.
def func_1(s):
    if (s == 'mapie') :
        return 1
        #The program returns 1.
    #State: s is a string consisting of lowercase Latin letters, and its length n satisfies 1 ≤ n ≤ 10^6. Additionally, s is not equal to 'mapie'.
    ans = 0
    while s.find('map') != -1:
        s = s[:s.find('map')] + s[s.find('map') + 2:]
        
        ans += 1
        
    #State: `s` is a string consisting of lowercase Latin letters, and its length `n` satisfies 1 ≤ n ≤ 10^6. `s` is not equal to 'mapie', does not contain the substring 'map', and may or may not contain the substring 'p'. `ans` is the number of times the substring 'map' was found and removed from `s`.
    while s.find('pie') != -1:
        s = s[:s.find('pie')] + s[s.find('pie') + 2:]
        
        ans += 1
        
    #State: `s` is a string consisting of lowercase Latin letters, and its length `n` is reduced by 3 * `ans` (1 ≤ n - 3 * `ans` ≤ 10^6). `s` does not contain the substrings 'map' or 'pie'. `s` is not equal to 'mapie'. `ans` is the total number of times the substring 'pie' was found and removed from `s`.
    return ans
    #The program returns the total number of times the substring 'pie' was found and removed from `s`.
#Overall this is what the function does:The function `func_1` takes a string `s` as input and returns an integer. If the string `s` is exactly 'mapie', the function returns 1. Otherwise, it removes all occurrences of the substrings 'map' and 'pie' from `s`, counting the total number of removals. The function then returns this count. After the function concludes, the string `s` will no longer contain the substrings 'map' or 'pie', and the returned value represents the total number of times these substrings were removed from `s`.

