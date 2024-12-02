#State of the program right berfore the function call: s is a string consisting of digits with a length not exceeding 1,000,000, and t is a non-empty string consisting of digits that may contain leading zeroes.
def func_1(s, t):
    t_set = set(t)
    n = ''
    for c in s:
        if c in t_set:
            n += c
        
    #State of the program after the  for loop has been executed: `n` is a string composed of characters from `s` that are also in `t_set`, and `s` can consist of any combination of digits. If `s` is empty, then `n` is an empty string. If `s` is non-empty, `n` contains the concatenation of all characters from `s` that exist in `t_set`.
    n += t
    return int(n)
    #The program returns the integer representation of the original string 'n', which is composed of characters from 's' that are also in 't_set', concatenated with 't'. If 's' is empty, 'n' becomes equal to 't'.
#Overall this is what the function does:The function accepts two strings, `s` and `t`. It creates a new string `n` by concatenating characters from `s` that also appear in `t`, followed by the string `t`. Finally, it returns the integer representation of this concatenated string. If `s` is empty, `n` will simply be `t`, and the function will return the integer value of `t`. This behavior includes handling of leading zeroes in `t`, where the integer conversion will ignore them.

