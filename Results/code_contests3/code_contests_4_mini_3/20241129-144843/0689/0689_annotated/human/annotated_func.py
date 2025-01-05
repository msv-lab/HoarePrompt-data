#State of the program right berfore the function call: S and T are strings consisting of lowercase English letters with lengths between 2 and 100, and |S| = |T|.
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function accepts two strings `s` and `t` of equal length consisting of lowercase English letters. It checks if `s` can be obtained by rotating `t` in any way (i.e., if `s` is a substring of `t` concatenated with itself). It prints 'Yes' if such a rotation exists and 'No' otherwise. However, it does not return any value but directly prints the result.

