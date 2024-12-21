#State of the program right berfore the function call: s is a string.
def func_1(s):
    result = ''
    for char in s:
        if char.isupper():
            result += char
        
    #State of the program after the  for loop has been executed: `s` is the original string, `result` is a string containing all the uppercase characters from `s`, in the order they appeared.
    return result
    #The program returns a string containing all the uppercase characters from the original string `s`, in the order they appeared
#Overall this is what the function does:The function accepts a string parameter `s` and returns a string containing all the uppercase characters from `s` in their original order. It does not modify the original string `s`. If the input string `s` is empty, the function will return an empty string. If the input string `s` contains no uppercase characters, the function will return an empty string. The function handles all possible edge cases, including strings with only lowercase characters, strings with only uppercase characters, strings with a mix of uppercase and lowercase characters, and empty strings, by returning a string containing only the uppercase characters from the input string `s`, in their original order.

