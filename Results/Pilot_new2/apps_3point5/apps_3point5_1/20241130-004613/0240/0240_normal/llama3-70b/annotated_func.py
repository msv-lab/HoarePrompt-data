#State of the program right berfore the function call: s and t are strings.**
def func_1(s, t):
    t_set = set(t)
    n = ''
    for c in s:
        if c in t_set:
            n += c
        
    #State of the program after the  for loop has been executed: `s`, `t`, `n` are strings and `t_set` is a set containing the unique elements of `t`. `n` is the concatenation of all characters in `s` that are present in `t`.
    n += t
    return int(n)
    #The program returns an integer which is the concatenation of all characters in string `s` that are present in set `t_set` followed by all elements of set `t_set`.
#Overall this is what the function does:The function accepts two string parameters s and t, creates a set of unique elements from string t, iterates through string s to concatenate characters present in both s and the set t_set, appends all elements from set t_set to the concatenated string, and finally returns the integer value of the concatenated string.

