#State of the program right berfore the function call: s is a string and ch is a single character string such that ch is present at least once in s.
def func_1(s, ch):
    first_index = s.find(ch)
    last_index = s.rfind(ch)
    if (first_index == -1 or last_index == -1 or first_index == last_index) :
        return s
        #The program returns string 's' which contains character 'ch' with the first occurrence at index 'first_index' and the last occurrence at index 'last_index', where 'first_index' is either -1 (if 'ch' is not found), or 'first_index' equals 'last_index' (if 'ch' appears only once), and 'last_index' is also either -1 (if 'ch' is not found) or equals 'first_index' (if 'ch' appears only once)
    #State of the program after the if block has been executed: `s` is a string, `ch` is a single character string present in `s`, `first_index` is the index of the first occurrence of `ch` in `s`, and `last_index` is the index of the last occurrence of `ch` in `s`. Additionally, `first_index` is not equal to -1, `last_index` is not equal to -1, and `first_index` is not equal to `last_index`, indicating that `ch` appears at least twice in `s` and both the first and last occurrences are valid indices.
    return s[:first_index] + s[first_index + 1:last_index] + s[last_index + 1:]
    #The program returns a string that is a modified version of `s`, where the first and last occurrences of `ch` are removed, and the parts of `s` before the first `ch`, between the first and last `ch` (excluding these `ch` characters), and after the last `ch` are concatenated together.
#Overall this is what the function does:The function accepts a string `s` and a character `ch`, and returns a modified string. If `ch` is not present in `s` or appears only once, the function returns the original string `s`. If `ch` appears at least twice in `s`, the function removes the first and last occurrences of `ch` from `s` and returns the resulting string, which is a concatenation of the parts of `s` before the first `ch`, between the first and last `ch` (excluding these `ch` characters), and after the last `ch`. The function handles edge cases where `ch` is not found in `s` or appears only once, and the returned string will be either the original string or the modified string with the first and last occurrences of `ch` removed.

