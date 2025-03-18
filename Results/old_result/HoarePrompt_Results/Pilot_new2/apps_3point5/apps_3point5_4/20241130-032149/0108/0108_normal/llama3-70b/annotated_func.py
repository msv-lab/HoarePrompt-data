#State of the program right berfore the function call: s is a string consisting of lowercase English letters.**
def func():
    s = input()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for char in alphabet:
        while char in s:
            res += char
            s = s.replace(char, chr(ord(char) + 1), 1)
        
    #State of the program after the  for loop has been executed: `s` is an empty string, `alphabet` contains all lowercase English letters, `res` is a string containing all lowercase English letters in consecutive order, `char` is the next character after 'z'
    if (len(res) == 26) :
        print(res)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`s` is an empty string, `alphabet` contains all lowercase English letters, `res` is a string containing all lowercase English letters in consecutive order, `char` is the next character after 'z'. If the length of `res` is 26, the string `res` containing all lowercase English letters in consecutive order is printed. Otherwise, if the length of `res` is not 26, -1 is printed, and no variables' values are changed.
#Overall this is what the function does:The function reads a string `s` consisting of lowercase English letters, iterates through the alphabet, and constructs a string `res` that contains all lowercase English letters in consecutive order by replacing occurrences in `s`. If the length of `res` becomes 26, it prints `res`; otherwise, it prints -1. The function does not explicitly return any value.

