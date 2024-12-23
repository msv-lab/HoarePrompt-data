#State of the program right berfore the function call: s is a string.
def func_1(s):
    result = ''
    for char in s:
        if char.isupper():
            result += char
        
    #State of the program after the  for loop has been executed: `s` is the original string, `char` is the last character of `s` if `s` is not empty, and `result` is a string containing all the uppercase letters from the original string `s`.
    return result
    #The program returns 'result' which is a string containing all the uppercase letters from the original string 's'.
#Overall this is what the function does:The function accepts a string `s` as input and returns a new string containing all the uppercase letters from the original string `s`. The original string `s` remains unchanged. If the input string `s` is empty, the function returns an empty string. If the input string contains no uppercase letters, the function returns an empty string. The function handles strings with a mix of uppercase and lowercase letters, as well as strings with non-alphabet characters, by filtering out non-uppercase letters and non-alphabet characters. The function does not perform any error checking on the input, so it assumes that the input will always be a string.

