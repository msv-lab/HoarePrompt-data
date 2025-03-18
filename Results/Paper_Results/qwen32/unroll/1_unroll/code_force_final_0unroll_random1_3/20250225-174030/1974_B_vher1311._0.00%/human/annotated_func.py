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
        
    #State: The list `s` will have characters replaced by those in `unique_chars` in reverse order if they were present initially, and new characters will be added to `unique_chars` and kept in `s`. The list `unique_chars` will contain all unique characters from `s` in the order they were first encountered, with new characters added to the beginning.
    return ''.join(unique_chars)
    #The program returns a string that is the concatenation of all unique characters from the list `s` in reverse order of their first encounter in `s`.
#Overall this is what the function does:The function takes a list of strings `s`, where each string consists of lowercase Latin letters. It returns a string containing all unique characters from the concatenated strings in `s`, ordered in reverse of their first appearance.

