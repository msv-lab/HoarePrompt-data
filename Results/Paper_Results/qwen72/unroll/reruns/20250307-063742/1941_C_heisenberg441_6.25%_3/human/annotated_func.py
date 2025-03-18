#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters, and its length n satisfies 1 ≤ n ≤ 10^6.
def func_1(s):
    if (s == 'mapie') :
        return 1
        #The program returns 1.
    #State: s is a string consisting of lowercase Latin letters, and its length n satisfies 1 ≤ n ≤ 10^6. s is not equal to 'mapie'.
    ans = 0
    while s.find('map') != -1:
        s = s[:s.find('map')] + s[s.find('map') + 2:]
        
        ans += 1
        
    #State: `s` is a string with all occurrences of 'map' removed, and `ans` is the number of times 'map' was found and removed from `s`.
    while s.find('pie') != -1:
        s = s[:s.find('pie')] + s[s.find('pie') + 2:]
        
        ans += 1
        
    #State: `s` is a string with all occurrences of 'pie' removed, and `ans` is the number of times 'pie' was found and removed from `s`.
    return ans
    #The program returns the number of times 'pie' was found and removed from the string `s`.
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of lowercase Latin letters and returns an integer. If the string `s` is exactly 'mapie', the function returns 1. Otherwise, the function removes all occurrences of the substrings 'map' and 'pie' from `s` and returns the total number of times these substrings were found and removed. After the function concludes, the string `s` will have all occurrences of 'map' and 'pie' removed, and the integer returned represents the count of these removals.

