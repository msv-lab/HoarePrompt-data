#State of the program right berfore the function call: s is a string.
def func_1(s):
    result = ''
    for char in s:
        if char.isupper():
            result += char
        
    #State of the program after the  for loop has been executed: `s` is a string, `char` is the last character of `s` if `s` is not empty, and `result` is a string containing all the uppercase characters from the original string `s`.
    return result
    #The program returns a string containing all the uppercase characters from the original string `s`.
#Overall this is what the function does:The function accepts a string parameter `s` and returns a string containing all the uppercase characters from `s`. If the input string `s` is empty, the function returns an empty string. If the input string `s` contains no uppercase characters, the function also returns an empty string. The original string `s` remains unchanged. The function handles strings with any combination of uppercase and lowercase characters, and it does not perform any error checking on the input, so it assumes that the input will always be a string.

