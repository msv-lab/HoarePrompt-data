#State of the program right berfore the function call: S and T are strings consisting of lowercase English letters, and |S| = |T| where 2 <= |S| <= 100.**
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function `func` takes two strings `S` and `T` as input, where both strings consist of lowercase English letters and have the same length between 2 and 100. It then checks if string `S` can be obtained by rotating string `T` and returns 'Yes' if it is possible, and 'No' otherwise.

