#State of the program right berfore the function call: s is a string that may contain both lowercase and uppercase characters.
def func_1(s):
    result = ''
    for char in s:
        if char.isupper():
            result += char
        
    #State of the program after the  for loop has been executed: `s` is a string that may contain both lowercase and uppercase characters, `result` is a string containing all uppercase characters from `s` in the order they appeared.
    return result
    #The program returns the string 'result' which contains all uppercase characters from string 's' in the order they appeared.
#Overall this is what the function does:The function accepts a string `s` and returns a new string containing all uppercase characters from `s` in the order they appeared. The function does not modify the original string `s`. If `s` contains no uppercase characters, the function will return an empty string. Additionally, the function does not handle any exceptions or edge cases such as non-string inputs or other types of characters.

