#State of the program right berfore the function call: S and T are strings consisting of lowercase English letters, and |S| = |T| where |X| denotes the length of the string X.**
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function `func` takes two strings `s` and `t` as input from the user and checks if string `s` can be obtained by rotating string `t`. It prints 'Yes' if it is possible, otherwise it prints 'No'. The function does not return any value.

