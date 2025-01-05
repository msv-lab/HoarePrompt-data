#State of the program right berfore the function call: S and T are strings consisting of lowercase English letters, with length between 2 and 100 (inclusive), and |S| = |T|.**
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function `func` reads two strings `S` and `T` from the user input, both consisting of lowercase English letters with lengths between 2 and 100 inclusive, where the length of `S` is equal to the length of `T`. It then checks if there exists an index `i` such that rotating `T` by `i` positions results in `S`. The function prints 'Yes' if such an index exists, and 'No' otherwise. The function does not explicitly return a value.

