#State of the program right berfore the function call: S and T are strings consisting of lowercase English letters, both having the same length where 2 <= |S| = |T| <= 100.
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function accepts two strings `s` and `t` of equal length consisting of lowercase English letters. It checks if `s` can be obtained by rotating `t` any number of times. If `s` is a rotation of `t`, it prints 'Yes'; otherwise, it prints 'No'. The function does not explicitly return any value, only prints the result.

