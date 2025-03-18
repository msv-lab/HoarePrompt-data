#State of the program right berfore the function call: s is a string consisting of lowercase English letters with a length in the range [1, 100000].
def func():
    s = input()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for char in alphabet:
        while char in s:
            res += char
            s = s.replace(char, chr(ord(char) + 1), 1)
        
    #State of the program after the  for loop has been executed: `s` is an empty string, `res` contains all characters from the original `s` in the order they were found, with characters from 'a' to the maximum character present in the original `s`, with no duplicates, and `char` is 'z' if the original `s` contained characters from 'a' to 'z'; if the original `s` did not contain any characters, `s` remains unchanged and `res` is empty.
    if (len(res) == 26) :
        print(res)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`s` is an empty string. If `res` contains all characters from 'a' to 'z', then `res` is 'abcdefghijklmnopqrstuvwxyz', `char` is 'z', and the length of `res` is 26. Otherwise, `res` is empty, `char` is 'z' if the original `s` contained characters from 'a' to 'z', and if the original `s` did not contain any characters, `s` remains unchanged, while the length of `res` is less than 26, and -1 is printed.
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase English letters and processes it to check for all characters from 'a' to 'z'. It constructs a new string `res` that contains the characters found in `s` in the order they appear, but without duplicates. If `s` contains all letters from 'a' to 'z', it prints `res` (which will be 'abcdefghijklmnopqrstuvwxyz'). If not all letters are present, it prints -1. The function does not explicitly handle cases where `s` might contain characters outside the range of 'a' to 'z', but it will still function correctly since it only processes lowercase English letters.

