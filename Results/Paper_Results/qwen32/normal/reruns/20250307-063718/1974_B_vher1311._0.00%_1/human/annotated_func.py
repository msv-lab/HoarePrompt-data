#State of the program right berfore the function call: s is a list of strings, where each string b consists of lowercase Latin letters and the length of each string b is between 1 and 2 \cdot 10^5. The length of the list s (number of test cases) is between 1 and 10^4, and the sum of the lengths of all strings in s does not exceed 2 \cdot 10^5.
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
        
    #State: `s` is modified with all occurrences of strings replaced by corresponding strings from `unique_chars`, `unique_chars` is a sorted list of all unique strings, `i` is the count of unique strings added during the loop, and `j` is the index of the last used string in `unique_chars` or `-1`.
    return ''.join(unique_chars)
    #The program returns a string which is the concatenation of all unique strings in the sorted list `unique_chars`.
#Overall this is what the function does:The function accepts a list of strings `s`, where each string consists of lowercase Latin letters. It processes the list to identify all unique characters, sorts them, and returns a string that is the concatenation of these sorted unique characters.

