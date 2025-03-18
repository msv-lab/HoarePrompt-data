#State of the program right berfore the function call: s is a non-empty string containing digits with a maximum length of 1,000,000, and t is a non-empty substring of s that may contain leading zeros.
def func_1(s, t):
    t_set = set(t)
    n = ''
    for c in s:
        if c in t_set:
            n += c
        
    #State of the program after the  for loop has been executed: `n` is a string that contains the concatenation of all characters from `s` that are also present in `t_set`, `s` is a non-empty string containing digits, `t` is a non-empty substring of `s`, `t_set` is a set of unique characters from `t`, and if `s` has no characters in `t_set`, then `n` remains an empty string.
    n += t
    return int(n)
    #The program returns the integer value of the string n, which is a concatenation of characters from s that are in t_set plus the substring t.
#Overall this is what the function does:The function accepts a non-empty string `s` containing digits and a non-empty substring `t` that may contain leading zeros. It constructs a new string by concatenating all characters from `s` that are also present in `t`, followed by the substring `t`, and returns the integer value of this concatenated string. If `s` has no characters that match those in `t`, the result will still include `t`, which could lead to returning an integer that represents just `t` (not prefixed by any characters from `s`).

