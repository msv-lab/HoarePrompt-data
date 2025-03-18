#State of the program right berfore the function call: s is a string that may contain both lowercase and uppercase substrings.
def func_1(s):
    result = ''
    for char in s:
        if char.isupper():
            result += char
        
    #State of the program after the  for loop has been executed: `result` is equal to the concatenation of all uppercase characters found in `s`, `s` can be any string, including an empty string. If `s` is empty, then `result` will also be an empty string.
    return result
    #The program returns the concatenation of all uppercase characters found in string 's', which may be an empty string. If 's' is empty, then 'result' will also be an empty string.
#Overall this is what the function does:The function accepts a string `s` and returns a new string that contains only the uppercase characters found in `s`. If `s` is empty or contains no uppercase characters, the function will return an empty string.

