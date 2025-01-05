#State of the program right berfore the function call: S and T are strings consisting of lowercase English letters, with lengths between 2 and 100, and |S| = |T|.
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function accepts two strings `s` and `t` of equal length, which consist of lowercase English letters. It checks if string `s` can be obtained by rotating string `t` any number of times. If `s` can be formed by rotating `t`, it prints 'Yes'; otherwise, it prints 'No'. The function does not explicitly return any value.

