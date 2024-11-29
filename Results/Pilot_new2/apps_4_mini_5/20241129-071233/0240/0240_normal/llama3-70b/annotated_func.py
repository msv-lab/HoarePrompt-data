#State of the program right berfore the function call: s is a string of digits (with a length not exceeding 1,000,000) representing the shuffled number received by Kate, and t is a non-empty substring of s that can contain leading zeroes.
def func_1(s, t):
    t_set = set(t)
    n = ''
    for c in s:
        if c in t_set:
            n += c
        
    #State of the program after the  for loop has been executed: `s` is a string of digits, `t` is a non-empty substring of `s`, `t_set` is a set containing the unique characters from `t`, and `n` is a string composed of all characters from `s` that are present in `t_set`. If `s` is empty, then `n` remains an empty string.
    n += t
    return int(n)
    #The program returns the integer value of 'n' which is the original 'n' concatenated with the substring 't' from the string of digits 's'
#Overall this is what the function does:The function accepts a string `s` of digits and a non-empty substring `t`, extracts the characters from `s` that are found in `t`, concatenates these characters with `t`, and returns the integer value of this concatenated string. If `s` contains characters not present in `t`, those characters will be ignored in the output. The length of `s` can be up to 1,000,000 characters.

