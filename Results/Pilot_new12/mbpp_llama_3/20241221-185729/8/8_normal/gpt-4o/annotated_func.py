#State of the program right berfore the function call: s is a string, and ch is a single character string that exists at least twice in s.
def func_1(s, ch):
    first_index = s.find(ch)
    last_index = s.rfind(ch)
    if (first_index == -1 or last_index == -1 or first_index == last_index) :
        return s
        #The program returns the string `s`, which may or may not contain the character `ch`, and if `ch` exists in `s`, it does so either multiple times or the information about its singles existence is overridden by the condition of multiple or no existence.
    #State of the program after the if block has been executed: `s` is a string, `ch` is a single character string that exists at least twice in `s`, `first_index` is the index of the first occurrence of `ch` in `s`, `last_index` is the index of the last occurrence of `ch` in `s`. `first_index` is not -1, `last_index` is not -1, and `first_index` is not equal to `last_index`.
    return s[:first_index] + s[first_index + 1:last_index] + s[last_index + 1:]
    #The program returns a string that is `s` with the first and last occurrences of character `ch` removed.
#Overall this is what the function does:The function accepts a string `s` and a character `ch`, and returns a modified string based on the occurrence of `ch` in `s`. If `ch` appears less than twice in `s`, the function returns the original string `s`. If `ch` appears at least twice in `s`, the function returns a new string that is `s` with the first and last occurrences of `ch` removed, potentially leaving `ch` in the string if it has more than two occurrences. The function effectively removes only the first and last occurrences of `ch` in `s`, without altering the rest of the string, thus handling edge cases where `ch` may appear multiple times consecutively or with other characters in between.

