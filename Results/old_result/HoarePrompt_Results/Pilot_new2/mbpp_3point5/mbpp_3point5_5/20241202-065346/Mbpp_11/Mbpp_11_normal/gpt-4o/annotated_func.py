#State of the program right berfore the function call: s is a string and ch is a single character string.**
def func_1(s, ch):
    first_index = s.find(ch)
    last_index = s.rfind(ch)
    if (first_index == -1 or last_index == -1 or first_index == last_index) :
        return s
        #The program returns the original string s
    #State of the program after the if block has been executed: *s is a string, ch is a single character string, first_index is the index of ch in s or -1 if ch is not found in s, last_index is the last index of ch in s or -1 if ch is not found in s. First_index is not -1, last_index is not -1, and first_index is not equal to last_index.
    return s[:first_index] + s[first_index + 1:last_index] + s[last_index + 1:]
    #The program returns a new string obtained by removing the characters at the positions of first_index and last_index from the original string s.
#Overall this is what the function does:The function `func_1` accepts two parameters: `s`, which is a string, and `ch`, which is a single character string. If the character `ch` is not found in string `s`, or if `ch` is found only once in `s`, the function returns the original string `s`. Otherwise, the function returns a new string obtained by removing the characters at the positions of the first occurrence and last occurrence of `ch` in the original string `s`.

