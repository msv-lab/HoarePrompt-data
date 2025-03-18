#State of the program right berfore the function call: s is a string of lowercase Latin letters with length n (1 ≤ n ≤ 10^6).
def func_1(s):
    if (s == 'mapie') :
        return 1
        #The program returns 1
    #State: s is a string of lowercase Latin letters with length n (1 ≤ n ≤ 10^6), and s is not equal to 'mapie'
    ans = 0
    while s.find('map') != -1:
        s = s[:s.find('map')] + s[s.find('map') + 2:]
        
        ans += 1
        
    #State: `s` with all 'map' substrings removed, `ans` is the count of removed 'map' substrings.
    while s.find('pie') != -1:
        s = s[:s.find('pie')] + s[s.find('pie') + 2:]
        
        ans += 1
        
    #State: s with all 'map' substrings removed, ans is the count of removed 'map' substrings.
    return ans
    #The program returns the count of removed 'map' substrings, which is stored in the variable 'ans'.
#Overall this is what the function does:The function `func_1` accepts a string `s` of lowercase Latin letters. It returns 1 if the string is exactly 'mapie'. Otherwise, it returns the count of 'map' and 'pie' substrings that are removed from the string.

