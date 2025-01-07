#State of the program right berfore the function call: s is a string consisting of lowercase English letters with a length between 1 and 100,000.
def func():
    s = input()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for char in alphabet:
        while char in s:
            res += char
            s = s.replace(char, chr(ord(char) + 1), 1)
        
    #State of the program after the  for loop has been executed: `s` is an empty string, `res` contains all characters from the original string `s` in the order of their first occurrence, with each character replaced by the next character in the alphabet, `char` is 'z' (the last character in `alphabet`).
    if (len(res) == 26) :
        print(res)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`s` is an empty string, if the length of `res` is equal to 26, the output is the value of `res`. Otherwise, if the length of `res` is less than 26, the value -1 has been printed.
#Overall this is what the function does:The function accepts no parameters and processes an internal string `s` input by the user, consisting of lowercase English letters. It constructs a new string `res` by replacing each character in `s` with the next character in the alphabet while preserving the order of their first occurrence. If `res` contains all 26 letters of the alphabet, it prints `res`; otherwise, it prints -1. If the input string lacks sufficient unique characters, the function will print -1, indicating that not all letters from 'a' to 'z' were represented.

