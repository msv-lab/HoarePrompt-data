#State of the program right berfore the function call: S and T are strings consisting of lowercase English letters, and both have the same length between 2 and 100 characters.
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function accepts two strings `s` and `t` of equal length consisting of lowercase English letters. It checks if string `s` can be obtained by rotating string `t` and returns 'Yes' if it can be obtained through rotation, otherwise it returns 'No'. The function reads the input directly from the user.

