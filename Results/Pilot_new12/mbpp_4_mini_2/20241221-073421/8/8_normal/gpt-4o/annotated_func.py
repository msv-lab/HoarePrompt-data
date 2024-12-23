#State of the program right berfore the function call: s is a string and ch is a string of length 1 (a single character).
def func_1(s, ch):
    first_index = s.find(ch)
    last_index = s.rfind(ch)
    if (first_index == -1 or last_index == -1 or first_index == last_index) :
        return s
        #The program returns the string `s`
    #State of the program after the if block has been executed: *`s` is a string, `ch` is a string of length 1, `first_index` is the index of the first occurrence of `ch` in `s`, `last_index` is the index of the last occurrence of `ch` in `s`, and both `first_index` and `last_index` are not -1, and they are not equal to each other (i.e., `first_index` is less than `last_index`).
    return s[:first_index] + s[first_index + 1:last_index] + s[last_index + 1:]
    #The program returns the string `s` with the first and last occurrence of character `ch` removed, using the indices `first_index` and `last_index` to slice the string appropriately.
#Overall this is what the function does:The function accepts a string `s` and a single character `ch`. It searches for the first and last occurrences of `ch` in `s`. If either occurrence is not found (i.e., `ch` does not exist in `s`), or if both occurrences are the same (indicating that `ch` appears only once in `s`), the function returns the string `s` unchanged. Otherwise, it returns a new string created by removing the first and last occurrences of `ch` from `s`. The function does not modify the original string `s` and handles cases where `s` might not contain `ch`, as well as where `ch` appears only once.

