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
        
    #State: `s` is a string where all characters have been replaced by the last unique character in `unique_chars`. `unique_chars` is a sorted list of unique characters from the original string `s`, possibly with some characters from `s` that were not initially in `unique_chars` inserted at the beginning. `i` is the length of `unique_chars`. `j` is -1.
    return ''.join(unique_chars)
    #The program returns a string that is the concatenation of all characters in the sorted list `unique_chars`.
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of lowercase Latin letters and returns a string containing all unique characters from `s`, sorted in ascending order. After the function concludes, the original string `s` is modified such that all characters are replaced by the last unique character in the sorted list of unique characters from `s`. The list `unique_chars` is a sorted list of unique characters from the original string `s`, with some characters from `s` that were not initially in `unique_chars` possibly inserted at the beginning. The final state of the program is that `s` is a string where all characters have been replaced by the last unique character in `unique_chars`, and `unique_chars` is a list that may contain additional characters from `s` at the beginning.

