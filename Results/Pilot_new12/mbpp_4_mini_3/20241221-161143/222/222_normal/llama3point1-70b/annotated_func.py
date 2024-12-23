#State of the program right berfore the function call: s is a string that may contain lowercase substrings.
def func_1(s):
    result = ''
    for char in s:
        if char.isupper():
            result += char
        
    #State of the program after the  for loop has been executed: `s` is a string, `result` is a string containing all uppercase letters found in `s`. If `s` has no uppercase letters, `result` remains an empty string.
    return result
    #The program returns the string containing all uppercase letters found in 's', or an empty string if 's' has no uppercase letters.
#Overall this is what the function does:The function `func_1` accepts a string `s` and extracts all uppercase letters from it. It constructs a new string, `result`, that contains only these uppercase letters. If there are no uppercase letters in `s`, the `result` will be an empty string. The function effectively filters the input string for uppercase characters and returns the filtered string, ensuring to handle cases where `s` may consist entirely of lowercase letters or be empty. It does not account for non-letter characters; if any uppercase letters exist alongside such characters, only the uppercase letters are retained in the output.

