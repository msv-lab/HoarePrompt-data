#State of the program right berfore the function call: S and T are strings consisting of lowercase English letters, and |S| = |T| where |X| denotes the length of string X.**
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function takes two strings S and T as input, compares characters in both strings at corresponding positions, and prints 'Yes' if there is a rotation of T that matches S, otherwise it prints 'No'. The function does not handle any exceptions or edge cases related to input validation or string manipulation.

