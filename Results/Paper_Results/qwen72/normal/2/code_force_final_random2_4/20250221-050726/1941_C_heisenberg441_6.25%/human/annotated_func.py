#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters.
def func_1(s):
    if (s == 'mapie') :
        return 1
        #The program returns 1.
    #State: s is a string consisting of lowercase Latin letters, and s is not equal to 'mapie'
    ans = 0
    while s.find('map') != -1:
        s = s[:s.find('map')] + s[s.find('map') + 2:]
        
        ans += 1
        
    #State: `s` is a string consisting of lowercase Latin letters and does not contain the substring 'map', `ans` is the number of times the substring 'map' was found and removed from `s`.
    while s.find('pie') != -1:
        s = s[:s.find('pie')] + s[s.find('pie') + 2:]
        
        ans += 1
        
    #State: `s` no longer contains the substring 'pie', and `ans` is the number of times the substring 'pie' was found and removed from `s`.
    return ans
    #The program returns the number of times the substring 'pie' was found and removed from `s`.
#Overall this is what the function does:The function `func_1` takes a string `s` consisting of lowercase Latin letters as input. If `s` is exactly "mapie", the function returns 1. Otherwise, it removes all occurrences of the substrings "map" and "pie" from `s`, counting the total number of removals. The function then returns this count. After the function concludes, `s` will no longer contain the substrings "map" or "pie", and the return value represents the number of times these substrings were found and removed.

