#State of the program right berfore the function call: s is a string and ch is a single character string.
def func_1(s, ch):
    first_index = s.find(ch)
    last_index = s.rfind(ch)
    if (first_index == -1 or last_index == -1 or first_index == last_index) :
        return s
        #The program returns string 's'
    #State of the program after the if block has been executed: `s` is a string, `ch` is a single character string, `first_index` is either the lowest index where `ch` is found in `s` or -1 if `ch` is not found in `s`; `last_index` is the highest index of `ch` in `s` or -1 if `ch` is not found in `s`. The condition `first_index != -1 and last_index != -1 and first_index != last_index` is false.
    return s[:first_index] + s[first_index + 1:last_index] + s[last_index + 1:]
    #The program returns a substring of 's' excluding the characters at 'first_index' and 'last_index'
#Overall this is what the function does:The function `func_1` accepts a string `s` and a single character string `ch`, and returns the original string `s` if `ch` is not found or found only once. Otherwise, it returns a substring of `s` with the characters at the first and last occurrence of `ch` removed.

