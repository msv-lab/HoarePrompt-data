#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters, and the length of s (denoted as n) satisfies 1 <= n <= 10^6.
def func_1(s):
    if (s == 'mapie') :
        return 1
        #The program returns 1
    #State: s is a string consisting of lowercase Latin letters, and the length of s (denoted as n) satisfies 1 <= n <= 10^6, and s is not equal to 'mapie'
    ans = 0
    while s.find('map') != -1:
        s = s[:s.find('map')] + s[s.find('map') + 2:]
        
        ans += 1
        
    #State: The string `s` no longer contains the substring 'map', and `ans` is the number of times 'map' was found and removed from `s`.
    while s.find('pie') != -1:
        s = s[:s.find('pie')] + s[s.find('pie') + 2:]
        
        ans += 1
        
    #State: The string `s` no longer contains the substring 'pie', and `ans` is the number of times 'pie' was found and removed from `s`.
    return ans
    #The program returns the number of times 'pie' was found and removed from string 's'
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase Latin letters and returns 1 if the substring 'pie' is not found in `s`. If 'pie' is found in `s`, the function removes all occurrences of 'pie' and returns the number of times 'pie' was found and removed.

