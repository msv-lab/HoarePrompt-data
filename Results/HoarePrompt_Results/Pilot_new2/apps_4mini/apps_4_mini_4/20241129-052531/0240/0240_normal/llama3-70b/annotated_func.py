#State of the program right berfore the function call: s is a non-empty string of digits with a length not exceeding 1,000,000, and t is a non-empty substring of s that can contain leading zeroes.
def func_1(s, t):
    t_set = set(t)
    n = ''
    for c in s:
        if c in t_set:
            n += c
        
    #State of the program after the  for loop has been executed: `n` is a string formed by concatenating all characters from `s` that are present in `t_set`; `s` is a non-empty string of digits, `t` is a non-empty substring of `s`, and `t_set` contains the unique characters from `t`. If there are no characters in `s` that are in `t_set`, then `n` will be an empty string.
    n += t
    return int(n)
    #The program returns the integer value of the string 'n' which is formed by concatenating all characters from 's' that are present in 't_set' followed by the substring 't'.
#Overall this is what the function does:The function accepts a non-empty string of digits `s` and a non-empty substring `t`. It constructs a new string by concatenating all characters from `s` that are present in `t`, followed by the substring `t`. The function then returns the integer value of this resulting string. If no characters from `s` are found in `t`, the function will return the integer value of `t` alone.

