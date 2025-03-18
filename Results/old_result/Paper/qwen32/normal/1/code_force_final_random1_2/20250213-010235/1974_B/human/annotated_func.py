#State of the program right berfore the function call: s is a list of strings where each string b consists of lowercase Latin letters and the length of each string b is between 1 and 2 \cdot 10^5. The length of the list s (number of test cases) is between 1 and 10^4. The sum of the lengths of all strings in s does not exceed 2 \cdot 10^5.
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
        
    #State: `s` is a list of strings where each string `b` consists of lowercase Latin letters, and each character in `b` that was originally in `unique_chars` has been replaced by the corresponding character from the end of `unique_chars` moving backwards. `unique_chars` is a list of all unique lowercase Latin characters found in `s`, potentially unsorted. `i` is the count of unique characters added during the loop, and `j` is `-1` if all characters in `unique_chars` have been used for replacement, otherwise it reflects the last position used for replacement.
    return ''.join(unique_chars)
    #The program returns a string that is the concatenation of all unique lowercase Latin characters found in the list `s`, potentially in an unsorted order.
#Overall this is what the function does:The function takes a list of strings as input, where each string consists of lowercase Latin letters. It returns a string containing all unique lowercase Latin characters found across all strings in the list, in an unspecified order.

