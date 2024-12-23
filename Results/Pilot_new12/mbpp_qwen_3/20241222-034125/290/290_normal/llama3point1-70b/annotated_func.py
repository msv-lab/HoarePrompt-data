#State of the program right berfore the function call: s is a string.
def func_1(s):
    words = s.split()
    for word in words:
        if len(word) > 1 and 'z' in word[1:-1]:
            return True
        
    #State of the program after the  for loop has been executed: `s` is a string, `words` is a list of substrings from `s`. If the function returns True during any iteration of the loop, it means that there exists at least one word in `words` that has a length greater than 1 and contains the character 'z' in the middle part of the word. Otherwise, the function returns None.
    return False
    #The program returns False
#Overall this is what the function does:The function `func_1` accepts a string `s` as a parameter. It splits the string into a list of words and checks each word to determine if it has a length greater than 1 and contains the character 'z' in the middle part of the word (i.e., excluding the first and last characters). If such a word is found, the function returns `True`. If no such word is found after checking all words, the function returns `False`. The function does not modify the input string `s` and only returns a boolean value.

