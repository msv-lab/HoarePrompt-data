#State of the program right berfore the function call: S and T are strings consisting of lowercase English letters, with lengths between 2 and 100, and |S| = |T|.
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function accepts two strings `s` and `t` consisting of lowercase English letters, both of equal length. It checks if `s` can be obtained by rotating `t` any number of times. If `s` is a rotation of `t`, the function prints 'Yes'; otherwise, it prints 'No'. It does not return any value.

