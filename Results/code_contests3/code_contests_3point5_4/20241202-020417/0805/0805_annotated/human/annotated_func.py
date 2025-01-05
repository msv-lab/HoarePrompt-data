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
        
    #State of the program after the  for loop has been executed: N is an integer within the specified range, S is a string of uppercase English letters, strings is an empty string, new_strings is a transformed string based on the shifting of characters
    print(new_strings)
#Overall this is what the function does:The function `func` takes user input for an integer `n` and a string of uppercase English letters `strings`. It then shifts each letter in `strings` by `n` positions cyclically in the alphabet and prints the resulting transformed string `new_strings`. The function does not handle cases where `n` is outside the range 0 to 26, and it assumes the input string `strings` consists only of uppercase English letters.

