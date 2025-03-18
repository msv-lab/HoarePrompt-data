#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters, and its length n satisfies 1 \le n \le 2 \cdot 10^5.
def func_1(s):
    unique_chars = sorted(list({char for char in s}))
    i, j = 0, len(unique_chars) - 1
    for char in s:
        if char in unique_chars:
            s = s.replace(char, unique_chars[j])
            j -= 1
        else:
            unique_chars.insert(i, char)
            i += 1
            j += 1
        
    #State: `s` is a string where all characters have been replaced by the last character in the `unique_chars` list, and `unique_chars` contains all unique characters from the initial `s` in their original order, plus any characters that were not in `unique_chars` initially, inserted at the beginning of the list. `i` is the number of unique characters that were not in the initial `unique_chars` list, and `j` is `len(unique_chars) - 1` minus the number of unique characters in the initial `s`.
    return ''.join(unique_chars)
    #The program returns a string that is a concatenation of all unique characters from the initial `s` in their original order, plus any characters that were not in `unique_chars` initially, inserted at the beginning of the list.
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of lowercase Latin letters and returns a new string that contains all unique characters from `s` in their original order, followed by any characters from `s` that were not initially in the set of unique characters, inserted at the beginning of the list. The original string `s` is modified such that all characters are replaced by the last character in the `unique_chars` list, but this modification is not returned.

