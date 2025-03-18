#State of the program right berfore the function call: s is a list of strings, where each string b in s consists of lowercase Latin letters and represents the result of encoding an original string s. The length of each string b is between 1 and 2 \cdot 10^5, and the total length of all strings in s does not exceed 2 \cdot 10^5. Additionally, s contains between 1 and 10^4 strings, each representing a separate test case.
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
        
    #State: `s` is a list of strings where each character in the strings of `s` has been replaced by characters from `unique_chars` in reverse order, and `unique_chars` contains all unique characters from `s` in the order they were first encountered or already present.
    return ''.join(unique_chars)
    #The program returns a string that is the concatenation of all unique characters from the list `s` in the order they were first encountered or already present.
#Overall this is what the function does:The function accepts a list of strings `s`, where each string consists of lowercase Latin letters. It returns a single string that is the concatenation of all unique characters from the list `s` in the order they were first encountered.

