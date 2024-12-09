#State of the program right berfore the function call: s is a string that may contain lowercase substrings.
def func_1(s):
    result = ''
    for char in s:
        if char.isupper():
            result += char
        
    #State of the program after the  for loop has been executed: `s` is a string, `result` is a string containing all the uppercase characters from `s` in the order they appear. If `s` is empty, then `result` remains an empty string.
    return result
    #The program returns the string 'result' containing all the uppercase characters from 's' in the order they appear. If 's' is empty, then 'result' remains an empty string.
#Overall this is what the function does:The function accepts a string `s` and returns a string containing all uppercase characters from `s` in the order they appear. If `s` is empty or contains no uppercase letters, the function returns an empty string.

