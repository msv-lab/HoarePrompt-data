#State of the program right berfore the function call: S and T are strings of lowercase English letters with lengths between 2 and 100, and |S| = |T|.
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function accepts two strings `s` and `t` of equal length and checks if string `s` can be obtained by rotating string `t`. It returns 'Yes' if `s` is a rotation of `t`, and 'No' otherwise. Note that the function uses `raw_input()` for input but does not handle any potential errors related to input validity or unexpected formats.

