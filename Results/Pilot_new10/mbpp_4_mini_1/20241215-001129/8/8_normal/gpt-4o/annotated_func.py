#State of the program right berfore the function call: s is a string and ch is a single character string.
def func_1(s, ch):
    first_index = s.find(ch)
    last_index = s.rfind(ch)
    if (first_index == -1 or last_index == -1 or first_index == last_index) :
        return s
        #The program returns the string `s`, which can be any string as `ch` is not found or appears an equal number of times (first and last occurrences are the same).
    #State of the program after the if block has been executed: *`s` is a string, `ch` is a single character string, `first_index` is the index of the first occurrence of `ch` in `s`, `last_index` is the index of the last occurrence of `ch` in `s`, both `first_index` and `last_index` are not equal to -1, and `first_index` is not equal to `last_index` (indicating that `ch` occurs more than once in `s`).
    return s[:first_index] + s[first_index + 1:last_index] + s[last_index + 1:]
    #The program returns the string 's' with the first and last occurrences of 'ch' removed, where 'first_index' is the index of the first occurrence of 'ch' in 's', and 'last_index' is the index of the last occurrence of 'ch' in 's', and both occurrences exist.
#Overall this is what the function does:The function accepts a string `s` and a single character `ch`, returning `s` unchanged if `ch` is not found in `s`, or if `ch` appears only once in `s`. If `ch` occurs more than once, the function returns the string `s` with the first and last occurrences of `ch` removed.

