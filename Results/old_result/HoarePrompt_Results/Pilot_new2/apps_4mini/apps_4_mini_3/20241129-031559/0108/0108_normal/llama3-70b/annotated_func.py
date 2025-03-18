#State of the program right berfore the function call: s is a string consisting of lowercase English letters with a length between 1 and 100,000 (1 ≤ |s| ≤ 10^5).
def func():
    s = input()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for char in alphabet:
        while char in s:
            res += char
            s = s.replace(char, chr(ord(char) + 1), 1)
        
    #State of the program after the  for loop has been executed: `s` is an empty string, `res` contains repeated instances of each character from 'a' to 'z' based on their occurrences in the original string, `char` is 'z', and the original `s` must have contained characters from 'a' to 'z'.
    if (len(res) == 26) :
        print(res)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`s` is an empty string. If the length of `res` is equal to 26, then the value of `res` is printed. Otherwise, `s` remains an empty string, `res` contains repeated instances of each character from 'a' to 'z' based on their occurrences in the original string, `char` is 'z', and the length of `res` is not equal to 26.
#Overall this is what the function does:The function accepts a string `s` composed of lowercase English letters and processes it to create a new string `res` consisting of repeated instances of each character from 'a' to 'z' based on their occurrences in `s`. If `s` contains all 26 letters of the English alphabet at least once, the function prints `res`; otherwise, it prints -1. Additionally, if `s` contains any characters outside the range of 'a' to 'z', those characters will not affect the output since only the first occurrence of each letter is replaced.

