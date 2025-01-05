#State of the program right berfore the function call: S and T are strings consisting of lowercase English letters, and |S| = |T| where 2 <= |S| <= 100.
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function accepts two strings `s` and `t`, both of equal length consisting of lowercase English letters. It checks if string `s` can be obtained by rotating string `t` and returns 'Yes' if it can, or 'No' otherwise. The function does not handle cases where the input strings do not meet the specified conditions.

