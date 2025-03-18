#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters. The string s represents the result of encoding some original string using the specified algorithm, and the length of s is at least 1.
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
        
    #State: The loop will continue until all characters in `s` have been processed or `j` becomes less than 0. After all iterations, `i` will be equal to the number of unique characters in `s` (or 1 if there are no unique characters), `j` will be equal to `len(unique_chars)`, and `s` will be modified such that any character in `s` that exists in `unique_chars` will be replaced according to the last value of `j` before the replacement operation. Characters not in `unique_chars` will be inserted into `unique_chars` at the correct position, and `j` will be adjusted accordingly.
    return ''.join(unique_chars)
    #The program returns a string where each character in the original string `s` that exists in `unique_chars` is replaced by the corresponding character from `unique_chars` based on its last occurrence index, and characters not in `unique_chars` are inserted into `unique_chars` at their correct positions with `j` being set to the length of `unique_chars`.
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase Latin letters. It returns a new string where each character in `s` that appears in the resulting `unique_chars` list is replaced by the corresponding character from `unique_chars` based on its last occurrence index in `s`. Characters not present in `unique_chars` are inserted into `unique_chars` at their correct positions, and `j` is set to the length of `unique_chars`.

