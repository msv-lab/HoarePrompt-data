#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters. The string s represents the result of encoding some original string using the specified algorithm, where the length of s is at least 1 and does not exceed 2 * 10^5.
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
        
    #State: The final state of `s` will be a string where each character has been replaced by another character from `unique_chars` based on the order of appearance. `unique_chars` will contain all unique characters from the final `s` in the order they appeared. `i` will be equal to the number of unique characters in `unique_chars`, and `j` will be -1.
    return ''.join(unique_chars)
    #The program returns a string composed of all unique characters from the final state of 's' in the order they appeared.
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase Latin letters. It processes `s` by replacing each character with another character from a list of unique characters based on their order of appearance. After processing, it returns a string containing all unique characters from the processed `s` in the order they appeared.

