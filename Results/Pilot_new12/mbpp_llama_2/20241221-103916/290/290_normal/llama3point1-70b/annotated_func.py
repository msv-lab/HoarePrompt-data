#State of the program right berfore the function call: s is a string.
def func_1(s):
    words = s.split()
    for word in words:
        if len(word) > 1 and 'z' in word[1:-1]:
            return True
        
    #State of the program after the  for loop has been executed: `s` is the original string, `words` is the list of words from string `s`, the function returns `True` if any word in `words` has 'z' in its middle characters, otherwise it returns `None`.
    return False
    #The program returns False
#Overall this is what the function does:The function `func_1` accepts a string `s` as input, splits it into a list of words, and checks each word for the presence of 'z' in its middle characters. If any word contains 'z' in its middle characters, the function immediately returns `True`. If no such word is found after checking all words, the function returns `False`. The original string `s` remains unchanged throughout the process. The function handles edge cases where the input string is empty or contains single-character words, and it correctly identifies the presence of 'z' in multi-character words. The function does not perform any error checking on the input type, so it assumes that the input will always be a string.

