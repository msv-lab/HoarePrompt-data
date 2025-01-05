#State of the program right berfore the function call: S and T are strings consisting of lowercase English letters, both of length between 2 and 100, and |S| = |T|.
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function accepts two strings `s` and `t` of equal length (between 2 and 100 characters) and checks if `s` can be obtained by rotating `t`. It returns 'Yes' if `s` can be formed by rotating `t`, or 'No' if it cannot. The function does not explicitly handle cases where the input strings do not meet the specified length constraints.

