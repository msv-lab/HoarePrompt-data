#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters, and the length of s is between 1 and 2 \cdot 10^5.
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
        
    #State: After all iterations of the loop, `s` will consist of the last unique character in the original `unique_chars` list repeated for the length of the original `s`. The `unique_chars` list will contain all unique characters from the original `s`, including any characters that were not initially in `unique_chars` but were added during the loop execution, and it will be in the order they were processed. The indices `i` and `j` will be such that `i` is equal to the number of unique characters that were not originally in `unique_chars` and were added during the loop, and `j` will be `len(unique_chars) - 1` minus the number of unique characters that were replaced in `s`.
    return ''.join(unique_chars)
    #The program returns a string consisting of all unique characters from the original `s`, including any characters that were not initially in `unique_chars` but were added during the loop, in the order they were processed.
#Overall this is what the function does:The function `func_1` takes a string `s` consisting of lowercase Latin letters and returns a new string containing all unique characters from `s` in the order they were first encountered. The returned string includes any characters that were not initially in the set of unique characters but were added during the function's execution. The original string `s` is modified during the function's execution, but the final state of `s` is not relevant to the function's output. The function ensures that the returned string contains each unique character exactly once, maintaining their first occurrence order.

