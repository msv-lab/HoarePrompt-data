#State of the program right berfore the function call: **
def func():
    s = input()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for char in alphabet:
        while char in s:
            res += char
            s = s.replace(char, chr(ord(char) + 1), 1)
        
    #State of the program after the  for loop has been executed: `s` is the final string after all replacements have been made, `alphabet` is 'abcdefghijklmnopqrstuvwxyz', `res` contains all characters from `alphabet` that were present in `s` before any replacements occurred, `char` is not present in the modified `s` string
    if (len(res) == 26) :
        print(res)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`s` is the final string after all replacements have been made, `alphabet` is 'abcdefghijklmnopqrstuvwxyz', `res` contains all characters from `alphabet` that were present in `s` before any replacements occurred, `char` is not present in the modified `s` string. If the current length of `res` is 26, the program continues execution. Otherwise, if the length of `res` is not equal to 26, -1 is printed.
#Overall this is what the function does:The function `func` reads a string input, iterates over the alphabet 'abcdefghijklmnopqrstuvwxyz', replaces each character in the input string with the next character in the alphabet, and constructs a result string containing all characters from the alphabet that were present in the input string before replacements. If the length of the result string is 26, it prints the result string. Otherwise, it prints -1. The function does not accept any parameters.

