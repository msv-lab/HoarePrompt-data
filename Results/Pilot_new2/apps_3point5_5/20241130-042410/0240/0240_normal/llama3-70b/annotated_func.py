#State of the program right berfore the function call: s is a string representing the number received by Kate, and t is a substring of s. Both s and t can contain leading zeroes.**
def func_1(s, t):
    t_set = set(t)
    n = ''
    for c in s:
        if c in t_set:
            n += c
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string representing the number received by Kate, `t` is a substring of `s` with leading zeroes, `t_set` is a set containing the unique characters of `t`, `n` is a string containing all characters of `s` that are also in `t_set`.
    n += t
    return int(n)
    #The program returns the integer value of string 'n', which contains all characters of string 's' that are also in the unique characters of substring 't', followed by the substring 't' with leading zeroes
#Overall this is what the function does:The function func_1 accepts two string parameters s and t. It iterates through string s and collects characters that are also present in substring t into a new string n. Then, it appends substring t to the end of n and returns the integer value of the resulting string n. The function handles cases where s and t can contain leading zeroes.

