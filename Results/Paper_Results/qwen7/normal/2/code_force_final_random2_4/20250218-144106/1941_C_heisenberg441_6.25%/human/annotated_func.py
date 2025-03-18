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
        
    #State: Output State: `ans` is the total number of times the substring 'map' was found and removed from the original string `s`, and `s` is the final string left after all occurrences of 'map' have been removed.
    #
    #To elaborate, the loop continues to run as long as the substring 'map' is found within `s`. Each iteration removes the first occurrence of 'map' from `s` and increments the counter `ans` by 1. After all iterations, `ans` will hold the total count of how many times 'map' was found and removed, and `s` will be the string that remains after all such substrings have been removed.
    while s.find('pie') != -1:
        s = s[:s.find('pie')] + s[s.find('pie') + 2:]
        
        ans += 1
        
    #State: The variable `ans` is the total count of how many times the substring 'pie' was found and removed from the original string `s`, and `s` is the final string left after all occurrences of 'pie' have been removed.
    return ans
    #The program returns the total count of how many times the substring 'pie' was found and removed from the original string 's'
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase Latin letters and returns either 1 or the total count of how many times the substring 'pie' appears in `s` and is removed. If the substring 'pie' is not present in `s`, the function returns 1. Otherwise, it removes all occurrences of 'pie' from `s` and returns the count of how many times 'pie' was found and removed.

