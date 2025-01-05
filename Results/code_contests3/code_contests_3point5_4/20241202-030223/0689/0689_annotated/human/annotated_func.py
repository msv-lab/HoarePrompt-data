#State of the program right berfore the function call: S and T are strings consisting of lowercase English letters, and |S| = |T| where 2 <= |S| <= 100.**
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function `func` reads two strings `S` and `T` as input, where both strings consist of lowercase English letters. The strings have equal lengths between 2 and 100. The function then checks if any rotation of string `T` matches string `S` and prints 'Yes' or 'No' accordingly. The function does not return any value explicitly.

