#State of the program right berfore the function call: S and T are strings consisting of lowercase English letters, and |S| = |T| where |X| denotes the length of string X.**
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function takes two input strings S and T, both consisting of lowercase English letters and having the same length. It then checks if there exists a rotation of string T that matches string S, and prints 'Yes' if such a rotation exists, otherwise 'No'.

