#State of the program right berfore the function call: s is a string.
def func_1(s):
    words = s.split()
    for word in words:
        if len(word) > 1 and 'z' in word[1:-1]:
            return True
        
    #State of the program after the  for loop has been executed: `s` is a string and `words` is a list of words from `s`. The function returns True if any word in `words` has a length greater than 1 and contains the letter 'z' in all positions except the first and last. Otherwise, the function returns None.
    return False
    #The program returns None
#Overall this is what the function does:The function `func_1` accepts a string `s` as a parameter and returns `True` if any word within the string has a length greater than 1 and contains the letter 'z' in any position except the first and last character. If no such word is found, the function returns `None`.

