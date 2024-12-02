#State of the program right berfore the function call: s is a string consisting of lowercase English letters.**
def func():
    s = input()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for char in alphabet:
        while char in s:
            res += char
            s = s.replace(char, chr(ord(char) + 1), 1)
        
    #State of the program after the  for loop has been executed: `s` is an empty string, `alphabet` is an empty string, `res` contains all the characters in the alphabet string concatenated together, `char` is the last character processed from the alphabet string
    if (len(res) == 26) :
        print(res)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`s` is an empty string, `alphabet` is an empty string, `res` contains all the characters in the alphabet string concatenated together, `char` is the last character processed from the alphabet string. If the length of `res` is 26, then all characters of the alphabet string are processed and the function terminates. If the length of `res` is not 26, the function prints -1 and does not affect any of the variables.
#Overall this is what the function does:The function `func` reads a string `s`, processes each character in the alphabet and replaces occurrences of that character in `s` with the next character in the alphabet. If a character is not present in `s`, it moves to the next character in the alphabet. The function then prints the concatenated characters from the alphabet processed in order. If all characters are processed (length of `res` is 26), it prints the concatenated alphabet. If not all characters are processed, it prints -1.

