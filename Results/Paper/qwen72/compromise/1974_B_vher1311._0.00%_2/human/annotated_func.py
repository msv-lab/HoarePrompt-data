#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters, and the length of s is a positive integer such that 1 <= len(s) <= 2 \cdot 10^5.
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
        
    #State: All characters in `s` are replaced by the last unique character in `unique_chars` before the loop starts, and `unique_chars` contains all the characters that were originally in `s`, sorted in the order they appeared in `s` before the loop started. `i` is the length of `unique_chars`, and `j` is 0.
    return ''.join(unique_chars)
    #The program returns a string containing all the unique characters from `s`, sorted in the order they appeared in `s` before the loop started.
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of lowercase Latin letters and returns a string containing all the unique characters from `s`, in the order they first appeared. The function modifies the input string `s` by replacing each character with the last unique character in the sorted list of unique characters from `s`. However, the final state of the program is such that the returned string is a sorted list of unique characters from `s`, in the order they appeared in the original string.

