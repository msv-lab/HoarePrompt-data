#State of the program right berfore the function call: s1 and s2 are non-empty strings consisting only of '0' and '1' characters, each with a length not exceeding 100000.
def func_1(s):
    q = (math.sqrt(5) + 1) / 2
    decimal = 0
    for (i, c) in enumerate(reversed(s)):
        decimal += int(c) * q ** i
        
    #State of the program after the  for loop has been executed: `s1` and `s2` are non-empty strings consisting only of '0' and '1' characters, each with a length not exceeding 100000, `q` is approximately 1.618033988749895, `decimal` is the sum of the decimal values of the characters in `s` weighted by powers of `q`, `s` is a non-empty string of '0' and '1' characters.
    return decimal
    #The program returns the sum of the decimal values of the characters in string `s` weighted by powers of `q`, where `q` is approximately 1.618033988749895 and `s` is a non-empty string consisting only of '0' and '1' characters
#Overall this is what the function does:The function accepts a string s consisting of '0' and '1' characters and returns the sum of the decimal values of the characters in string s weighted by powers of a constant q, approximately 1.618033988749895. If the string is empty, it returns 0. If the string contains characters other than '0' and '1', it raises a ValueError. The function does not enforce any length constraints on the input string.

