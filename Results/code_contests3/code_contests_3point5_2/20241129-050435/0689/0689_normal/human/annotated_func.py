#State of the program right berfore the function call: S and T are strings consisting of lowercase English letters with lengths between 2 and 100, and |S| = |T|.**
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function `func` reads two strings `s` and `t` of equal length from the user input. It then checks if string `s` can be obtained by rotating string `t` and prints 'Yes' if possible, 'No' otherwise. The function does not have any return value.

