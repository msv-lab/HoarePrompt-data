#State of the program right berfore the function call: N is an integer such that 0 <= N <= 26. S is a string consisting of uppercase English letters with length between 1 and 10^4.**
def func():
    n = int(input())
    strings = input()
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_strings = ''
    for s in strings:
        index = letters.index(s)
        
        added_index = index + n
        
        new_index = added_index % 26
        
        new_s = letters[new_index]
        
        new_strings += new_s
        
    #State of the program after the  for loop has been executed: `N` is an integer between 0 and 26, `S` is a string consisting of uppercase English letters, `letters` contains all uppercase English letters, `new_strings` contains the concatenated characters from `new_s` after processing all strings in `S`, `strings` is empty, `s` is the last string processed, `index` is the index of the last occurrence of `s` in `letters`, `added_index` is the result of adding the last `index` and `N`, `new_index` is the remainder of `added_index` divided by 26, `new_s` is assigned the character at index `new_index` in `letters`.
    print(new_strings)
#Overall this is what the function does:The function `func` takes user input for an integer `N` and a string `S` consisting of uppercase English letters. It processes each character in `S` by shifting it by `N` positions in the English alphabet, wrapping around from 'Z' to 'A' if necessary. The function then prints the modified string `new_strings`. The function does not return any specific output.

