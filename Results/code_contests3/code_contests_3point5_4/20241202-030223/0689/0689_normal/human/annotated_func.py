#State of the program right berfore the function call: S and T are strings consisting of lowercase English letters, and |S| = |T| where |X| denotes the length of string X.**
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function reads two strings `s` and `t` from the user input and checks if string `s` can be derived from string `t` by rotating it. It then prints 'Yes' if this condition is met, otherwise it prints 'No'. The function does not accept any parameters and does not return any value.

