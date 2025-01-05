#State of the program right berfore the function call: S and T are strings consisting of lowercase English letters, with lengths between 2 and 100, and |S| = |T|.
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function accepts two strings `s` and `t` of equal length consisting of lowercase English letters. It checks if `s` can be obtained by rotating `t` (i.e., moving characters from the beginning of `t` to the end). It prints 'Yes' if `s` can be formed from `t` by rotation, and 'No' otherwise.

