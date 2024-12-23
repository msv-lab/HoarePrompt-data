#State of the program right berfore the function call: s is a string.
def func_1(s):
    words = s.split()
    for word in words:
        if len(word) > 1 and 'z' in word[1:-1]:
            return True
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string, `words` is a list of substrings from the original string `s`, and the function returns `True` if any word in `words` has a length greater than 1 and contains 'z' in the substring from the second character to the second last character, otherwise the function returns `None`.
    return False
    #The program returns None
#Overall this is what the function does:The function `func_1` accepts a string `s` as input and returns `True` if any word in the string `s` (after splitting by spaces) has a length greater than 1 and contains the letter 'z' within the word, excluding the first and last characters. If no such word is found, the function returns `None`.

