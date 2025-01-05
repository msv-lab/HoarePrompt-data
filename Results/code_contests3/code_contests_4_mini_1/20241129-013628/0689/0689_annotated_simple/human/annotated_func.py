#State of the program right berfore the function call: S and T are strings consisting of lowercase English letters, and both strings have the same length, where the length is an integer between 2 and 100 inclusive.
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function accepts two strings `s` and `t`, both of equal length (between 2 and 100 characters) consisting of lowercase English letters. It checks if string `s` can be obtained by rotating string `t` (i.e., shifting characters in `t` around). If `s` can be formed by rotating `t`, it returns 'Yes'; otherwise, it returns 'No'. Note that the function does not handle cases where the inputs do not meet the expected conditions, such as non-string inputs or strings of different lengths, but it is expected to receive valid input as per the preconditions.

