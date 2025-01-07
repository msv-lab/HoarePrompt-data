#State of the program right berfore the function call: s is a string consisting of |s| small English letters, where 1 ≤ |s| ≤ 10^5.
def func():
    s = input()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for char in alphabet:
        while char in s:
            res += char
            s = s.replace(char, chr(ord(char) + 1), 1)
        
    #State of the program after the  for loop has been executed: `s` is empty or contains characters greater than 'z', `res` is the concatenation of all characters from 'a' to 'z' according to their occurrences in the original string, `char` is beyond 'z' (i.e., `char` is '{' in ASCII), indicating that all characters from 'a' to 'z' have been processed.
    if (len(res) == 26) :
        print(res)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`s` is empty or contains characters greater than 'z'; if the length of `res` is 26, then `res` is equal to "abcdefghijklmnopqrstuvwxyz", indicating that all characters from 'a' to 'z' have been processed. Otherwise, the length of `res` is less than 26, indicating that not all characters from 'a' to 'z' have been processed.
#Overall this is what the function does:The function accepts a string `s` of lowercase English letters, constructs a string by appending each letter from 'a' to 'z' according to their occurrences in `s`, and prints the constructed string if it contains all letters from 'a' to 'z'; otherwise, it prints -1. It ignores any characters in `s` that are not lowercase letters.

