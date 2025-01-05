#State of the program right berfore the function call: S and T are strings consisting of lowercase English letters with lengths between 2 and 100 inclusive.**
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function `func` reads two strings, S and T, from user input. It then checks if any rotation of string T matches string S. If a match is found, it prints 'Yes'; otherwise, it prints 'No'. The function does not explicitly return any value. The strings S and T consist of lowercase English letters with lengths between 2 and 100 inclusive.

