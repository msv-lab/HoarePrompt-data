#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters.
def func_1(s):
    if (s == 'mapie') :
        return 1
        #The program returns 1
    #State: s is a string consisting of lowercase Latin letters, and s is not equal to 'mapie'
    ans = 0
    while s.find('map') != -1:
        s = s[:s.find('map')] + s[s.find('map') + 2:]
        
        ans += 1
        
    #State: `s` is a string with all occurrences of 'map' removed, and `ans` is the number of times 'map' was found and removed from `s`.
    while s.find('pie') != -1:
        s = s[:s.find('pie')] + s[s.find('pie') + 2:]
        
        ans += 1
        
    #State: 
    return ans
    #The program returns the variable `ans`
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase Latin letters. It checks if `s` is exactly 'mapie' and returns 1 in that case. Otherwise, it removes all occurrences of the substrings 'map' and 'pie' from `s`, counting how many times these substrings are removed, and returns this count.

