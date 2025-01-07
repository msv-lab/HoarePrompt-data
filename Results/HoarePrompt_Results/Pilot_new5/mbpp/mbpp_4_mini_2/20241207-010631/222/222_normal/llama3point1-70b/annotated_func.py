#State of the program right berfore the function call: s is a string that may contain lowercase substrings.
def func_1(s):
    result = ''
    for char in s:
        if char.isupper():
            result += char
        
    #State of the program after the  for loop has been executed: `result` is a string containing all uppercase letters found in `s`, `s` is a string (may be empty), if `s` is empty, `result` is empty; otherwise, `result` contains only uppercase letters from `s`.
    return result
    #The program returns a string containing all uppercase letters found in 's'; if 's' is empty, 'result' is empty.
#Overall this is what the function does:The function accepts a string `s` and returns a string containing all uppercase letters found in `s`. If `s` is empty, it returns an empty string. If `s` contains no uppercase letters, the result will also be an empty string. The function ignores any lowercase letters and non-alphabetic characters.

