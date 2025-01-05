#State of the program right berfore the function call: S and T are strings consisting of lowercase English letters, and the length of S and T is between 2 and 100, inclusive.**
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function `func` reads two strings `s` and `t` from the user input. It then checks if any rotation of string `t` matches string `s`. If a rotation of `t` matches `s`, it prints 'Yes'; otherwise, it prints 'No'. The function does not accept any parameters and does not have an explicit return value.

