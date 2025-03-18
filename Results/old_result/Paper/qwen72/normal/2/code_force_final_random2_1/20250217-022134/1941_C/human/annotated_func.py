#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters, and its length n satisfies 1 ≤ n ≤ 10^6.
def func_1(s):
    if (s == 'mapie') :
        return 1
        #The program returns 1.
    #State: s is a string consisting of lowercase Latin letters, and its length n satisfies 1 ≤ n ≤ 10^6, and s is not equal to 'mapie'
    ans = 0
    while s.find('map') != -1:
        s = s[:s.find('map')] + s[s.find('map') + 2:]
        
        ans += 1
        
    #State: `s` is a string consisting of lowercase Latin letters and no longer contains the substring 'map', and its length n satisfies 1 ≤ n ≤ 10^6; `ans` is the number of times the substring 'map' was found and removed from the original string `s`.
    while s.find('pie') != -1:
        s = s[:s.find('pie')] + s[s.find('pie') + 2:]
        
        ans += 1
        
    #State: `s` is a string consisting of lowercase Latin letters, no longer contains the substring 'map', and does not contain the substring 'pie'; `ans` is the total number of times the substring 'pie' was found and removed from the original string `s`.
    return ans
    #The program returns the total number of times the substring 'pie' was found and removed from the original string `s`.
#Overall this is what the function does:The function `func_1` takes a string `s` consisting of lowercase Latin letters and returns the total number of times the substrings 'map' and 'pie' were found and removed from the string. If the string `s` is exactly 'mapie', the function immediately returns 1. Otherwise, it processes the string to remove occurrences of 'map' and 'pie', counting each removal, and returns the total count of these removals. After the function completes, the string `s` will no longer contain the substrings 'map' or 'pie'.

