#State of the program right berfore the function call: s is a string consisting of lowercase English letters.**
def func():
    s = input()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for char in alphabet:
        while char in s:
            res += char
            s = s.replace(char, chr(ord(char) + 1), 1)
        
    #State of the program after the  for loop has been executed: `s` is an empty string, `alphabet` is a string containing all lowercase English letters, `res` contains all characters from `alphabet` concatenated in order, and `char` is the last character in `alphabet`
    if (len(res) == 26) :
        print(res)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`s` is an empty string, `alphabet` is a string containing all lowercase English letters, `res` contains all characters from `alphabet` concatenated in order, `char` is the last character in `alphabet`, and the length of `res` is either 26 or not 26, depending on the condition of the if statement
#Overall this is what the function does:The function reads a string `s` consisting of lowercase English letters from the user input. It iterates over the alphabet, and for each character in the alphabet, it checks if that character exists in the input string `s`. If found, it appends that character to the result string `res` and replaces the character in `s` with the next character in the alphabet. Finally, if the length of `res` is 26, it prints out `res`; otherwise, it prints -1. The function does not explicitly return any value and operates solely on the input string `s`.

