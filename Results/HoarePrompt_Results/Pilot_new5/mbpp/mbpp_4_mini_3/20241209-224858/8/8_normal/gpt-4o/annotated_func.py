#State of the program right berfore the function call: s is a string and ch is a single character string.
def func_1(s, ch):
    first_index = s.find(ch)
    last_index = s.rfind(ch)
    if (first_index == -1 or last_index == -1 or first_index == last_index) :
        return s
        #The program returns the string 's' since either 'first_index' is -1, 'last_index' is -1, or both indices are equal, indicating that the character 'ch' is not found in 's' or appears only once.
    #State of the program after the if block has been executed: *`s` is a string, `ch` is a single character string, `first_index` is the index of the first occurrence of `ch` in `s`, and `last_index` is the index of the last occurrence of `ch` in `s`. Both `first_index` and `last_index` are not equal to -1, and they are not equal to each other.
    return s[:first_index] + s[first_index + 1:last_index] + s[last_index + 1:]
    #The program returns the string formed by concatenating the substring from the start of `s` to `first_index`, the substring from `first_index + 1` to `last_index`, and the substring from `last_index + 1` to the end of `s`.
#Overall this is what the function does:The function accepts a string `s` and a single character string `ch`. It returns the original string `s` if `ch` is not found in `s` or appears only once. If `ch` appears more than once, it returns a modified string with all occurrences of `ch` removed, except for the first and last occurrences.

