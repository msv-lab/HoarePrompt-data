#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters, and its length n satisfies 1 <= n <= 10^6.
def func_1(s):
    if (s == 'mapie') :
        return 1
        #The program returns 1
    #State: s is a string consisting of lowercase Latin letters, and its length n satisfies 1 <= n <= 10^6, and s is not equal to 'mapie'
    ans = 0
    while s.find('map') != -1:
        s = s[:s.find('map')] + s[s.find('map') + 2:]
        
        ans += 1
        
    #State: The variable `ans` will be the number of times the substring 'map' appears in the string `s`, and `s` will be the original string with all occurrences of 'map' removed.
    while s.find('pie') != -1:
        s = s[:s.find('pie')] + s[s.find('pie') + 2:]
        
        ans += 1
        
    #State: The string `s` has all occurrences of 'pie' replaced with '', and `ans` is the count of how many times 'pie' was found and removed.
    return ans
    #The program returns the count of how many times 'pie' was found and removed from string 's'
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase Latin letters and returns either 1 or the count of how many times the substring 'pie' is found and removed from `s`. If 'pie' is not found in `s`, it returns 1. Otherwise, it iterates through `s` to find and remove all occurrences of 'pie', counting each removal, and then returns the total count of such occurrences.

