#State of the program right berfore the function call: s is a string.
def func_1(s):
    result = ''
    for char in s:
        if char.isupper():
            result += char
        
    #State of the program after the  for loop has been executed: `s` is a string (possibly empty), `result` is a string containing all the uppercase letters from `s` in the order they appear, and `char` is the last uppercase letter processed or the next character to be processed if there are more uppercase letters.
    return result
    #The program returns the string 'result' which contains all the uppercase letters from 's' in the order they appear
#Overall this is what the function does:The function `func_1` accepts a string `s` as input and returns a new string `result` that contains all the uppercase letters from `s` in the order they appear. If `s` is empty or contains no uppercase letters, the function returns an empty string. The function iterates through each character in `s`, checks if the character is uppercase, and if so, appends it to `result`. No other transformations or operations are performed on the characters in `s`.

