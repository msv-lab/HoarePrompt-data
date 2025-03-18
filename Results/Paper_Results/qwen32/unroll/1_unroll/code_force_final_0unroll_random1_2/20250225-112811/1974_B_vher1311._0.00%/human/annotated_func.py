#State of the program right berfore the function call: s is a list of strings, where each string b consists of lowercase Latin letters, and the length of each string b is between 1 and 2 \cdot 10^5. The length of the list s (number of test cases) is between 1 and 10^4. The sum of the lengths of all strings in s does not exceed 2 \cdot 10^5.
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
        
    #State: `s` is transformed to a list where each string is replaced by the corresponding string from `unique_chars` in reverse order of their first appearance, and `unique_chars` contains all unique strings from the initial `s` in the order they were first encountered and then added to the list.
    return ''.join(unique_chars)
    #The program returns a string that is the concatenation of all unique strings from the initial `s` in the order they were first encountered.
#Overall this is what the function does:The function accepts a list of strings `s`, where each string consists of lowercase Latin letters. It returns a single string that is the concatenation of all unique characters from the initial list `s` in the order they were first encountered.

