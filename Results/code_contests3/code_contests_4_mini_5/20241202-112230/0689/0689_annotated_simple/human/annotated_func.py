#State of the program right berfore the function call: S and T are strings consisting of lowercase English letters, and both strings have a length between 2 and 100, inclusive, with |S| = |T|.
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function reads two strings `s` and `t` from user input, checks if `s` is a rotation of `t`, and prints "Yes" if it is, or "No" if it is not.

