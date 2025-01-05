#State of the program right berfore the function call: S and T are strings consisting of lowercase English letters, and both strings have the same length between 2 and 100 characters inclusive.
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function accepts two strings `s` and `t`, both consisting of lowercase English letters and of equal length between 2 and 100 characters. It checks if `s` can be obtained by rotating `t` in any way (i.e., if `s` is a rotation of `t`) and prints 'Yes' if it is, or 'No' if it is not. The function does not accept parameters directly but instead reads the input from the user.

