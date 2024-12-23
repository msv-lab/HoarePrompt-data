#State of the program right berfore the function call: s is a string and ch is a single character string.
def func_1(s, ch):
    first_index = s.find(ch)
    last_index = s.rfind(ch)
    if (first_index == -1 or last_index == -1 or first_index == last_index) :
        return s
        #The program returns string `s` where the condition (first_index == -1 or last_index == -1 or first_index == last_index) is true
    #State of the program after the if block has been executed: `s` is a string, `ch` is a single character string, `first_index` is either the index where `ch` is first found in `s` or -1 if `ch` is not found in `s`, `last_index` is the index of the last occurrence of `ch` in `s` or -1 if `ch` is not found in `s`. The condition `(first_index != -1 and last_index != -1 and first_index != last_index)` is true
    return s[:first_index] + s[first_index + 1:last_index] + s[last_index + 1:]
    #The program returns a string that is formed by slicing the initial string `s` and removing the substring from `first_index` to `first_index + last_index - first_index`, effectively removing the first and last occurrences of `ch` in `s`
#Overall this is what the function does:The function `func_1` accepts a string `s` and a single character string `ch`. It first finds the indices of the first and last occurrences of `ch` in `s`. If `ch` is not found in `s` or if the first and last occurrences of `ch` are the same, it returns the original string `s`. Otherwise, it returns a new string formed by removing the substring from the first occurrence of `ch` to the last occurrence of `ch` in `s`. This includes handling cases where `ch` is not found in `s` (in which case both `first_index` and `last_index` will be `-1`), and cases where the first and last occurrences of `ch` are the same (in which case only one instance of `ch` is removed).

