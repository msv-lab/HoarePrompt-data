#State of the program right berfore the function call: S and T are strings of lowercase English letters with length between 2 and 100, and |S| = |T|.**
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function `func` reads two strings `s` and `t` of lowercase English letters with lengths between 2 and 100, where the lengths of `s` and `t` are equal. It then checks if `s` can be obtained by rotating `t` and prints 'Yes' if it is possible, otherwise 'No'. The function does not accept any parameters and does not return any value.

