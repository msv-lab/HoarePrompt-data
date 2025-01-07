#State of the program right berfore the function call: s is a string that may contain lowercase substrings.
def func_1(s):
    result = ''
    for char in s:
        if char.isupper():
            result += char
        
    #State of the program after the  for loop has been executed: `result` contains all uppercase characters from `s`, `s` is a string, `char` is the last character processed in `s`, and if `s` is empty, `result` remains an empty string.
    return result
    #The program returns all uppercase characters from the string 's' as contained in 'result'
#Overall this is what the function does:The function accepts a string `s` and returns a new string that consists only of the uppercase characters found in `s`. If `s` contains no uppercase characters or is empty, the function will return an empty string.

