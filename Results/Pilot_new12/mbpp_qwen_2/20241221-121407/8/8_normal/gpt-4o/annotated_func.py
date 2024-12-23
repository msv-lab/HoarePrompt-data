#State of the program right berfore the function call: s is a string and ch is a single character string.
def func_1(s, ch):
    first_index = s.find(ch)
    last_index = s.rfind(ch)
    if (first_index == -1 or last_index == -1 or first_index == last_index) :
        return s
        #`s` is a string, `ch` is a single character string, `first_index` is either the index of the first occurrence of `ch` in `s` or -1 if `ch` is not found in `s`; `last_index` is the index of the last occurrence of `ch` in `s` or -1 if `ch` is not found in `s`. Either `first_index` and `last_index` are both -1, or they are equal, indicating that `ch` occurs at most once in `s`. The program returns `s`
    #State of the program after the if block has been executed: `s` is a string, `ch` is a single character string, `first_index` is either the index of the first occurrence of `ch` in `s` or -1 if `ch` is not found in `s`; `last_index` is the index of the last occurrence of `ch` in `s` or -1 if `ch` is not found in `s`. The first index is not -1 and is different from the last index, and at least one of them is not -1
    return s[:first_index] + s[first_index + 1:last_index] + s[last_index + 1:]
    #`The program returns the string `s` with the character `ch` removed, considering the first and last indices where `ch` appears in `s`
#Overall this is what the function does:The function `func_1` accepts a string `s` and a single character string `ch`. It first finds the indices of the first and last occurrences of `ch` in `s`. If `ch` is not found in `s` (both indices are -1), it returns `s` unchanged. If `ch` is found one or more times, it returns `s` with all occurrences of `ch` removed. This is achieved by constructing a new string that excludes the characters at the first and last indices where `ch` appears, along with any characters between them.

