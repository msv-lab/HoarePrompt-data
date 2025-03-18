#State of the program right berfore the function call: s is a string, and ch is a single character string.
def func_1(s, ch):
    first_index = s.find(ch)
    last_index = s.rfind(ch)
    if (first_index == -1 or last_index == -1 or first_index == last_index) :
        return s
        #The program returns the string 's' regardless of the indices of 'ch' in 's', which can be either -1 or equal, indicating the absence of 'ch' or a single occurrence.
    #State of the program after the if block has been executed: *`s` is a string, `ch` is a single character string, `first_index` is the index of the first occurrence of `ch` in `s`, `last_index` is the index of the last occurrence of `ch` in `s`. Both `first_index` and `last_index` are not -1, and `first_index` is not equal to `last_index`.
    return s[:first_index] + s[first_index + 1:last_index] + s[last_index + 1:]
    #The program returns a new string formed by removing the first and last occurrences of the character 'ch' in the string 's'. Specifically, it includes the substring from the start of 's' to the index before 'first_index', followed by the substring from the index after 'first_index' to the index before 'last_index', and finally the substring from the index after 'last_index' to the end of 's'.
#Overall this is what the function does:The function accepts a string `s` and a single character string `ch`. It returns the original string `s` if `ch` is not found or occurs only once in `s`. If `ch` occurs more than once, it returns a new string with the first and last occurrences of `ch` removed. The function does not handle the case where `ch` is an empty string; in such a case, it would raise a ValueError due to the nature of the find and rfind methods.

