#State of the program right berfore the function call: s is a string that may contain both lowercase and uppercase characters.
def func_1(s):
    result = ''
    for char in s:
        if char.isupper():
            result += char
        
    #State of the program after the  for loop has been executed: `s` is a string, `result` is the concatenation of all uppercase characters in `s`. If `s` is empty, then `result` remains an empty string.
    return result
    #The program returns the concatenation of all uppercase characters in string 's', which is stored in the variable 'result'. If 's' is empty, 'result' remains an empty string.
#Overall this is what the function does:The function accepts a single string parameter `s` and returns a new string that consists of the concatenation of all uppercase characters found in `s`. If `s` contains no uppercase characters or is empty, the function will return an empty string. The implementation only processes the characters that are uppercase and ignores all other characters without any error handling or special cases regarding non-alphabetic characters.

