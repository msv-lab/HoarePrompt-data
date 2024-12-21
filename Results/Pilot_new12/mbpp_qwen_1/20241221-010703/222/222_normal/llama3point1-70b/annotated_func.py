#State of the program right berfore the function call: s is a string.
def func_1(s):
    result = ''
    for char in s:
        if char.isupper():
            result += char
        
    #State of the program after the  for loop has been executed: `s` is a string, `result` is a string containing all the uppercase characters from `s` in the order they appear.
    return result
    #`The program returns the string 'result' which contains all the uppercase characters from 's' in the order they appear
#Overall this is what the function does:This function accepts a string `s` and returns a new string containing only the uppercase characters from `s` in the order they appear. It iterates through each character in `s`, checks if the character is uppercase, and if so, appends it to the `result` string. The function does not modify the original string `s`.

