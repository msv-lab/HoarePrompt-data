#State of the program right berfore the function call: s is a string consisting of 1 to 100,000 lowercase English letters.
def func():
    s = input()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for char in alphabet:
        while char in s:
            res += char
            s = s.replace(char, chr(ord(char) + 1), 1)
        
    #State of the program after the  for loop has been executed: `s` is an empty string, `res` contains all characters from the original `s`, `char` is 'z' + 1.
    if (len(res) == 26) :
        print(res)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`s` is an empty string, `res` contains all characters from the original `s`, and `char` is 'z' + 1. If the length of `res` is equal to 26, no further action occurs. If the length of `res` is not equal to 26, -1 is printed.
#Overall this is what the function does:The function accepts a string `s` consisting of 1 to 100,000 lowercase English letters and constructs a new string `res` by replacing each character in `s` with its subsequent character in the alphabet (e.g., 'a' becomes 'b', 'b' becomes 'c', and so on). After processing all characters, if `res` contains exactly 26 characters (indicating that all letters from 'a' to 'z' were present in `s`), it prints `res`. If not all letters are present, it prints `-1`.

