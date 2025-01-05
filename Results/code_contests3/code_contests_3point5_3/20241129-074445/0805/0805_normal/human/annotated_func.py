#State of the program right berfore the function call: **
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `strings` is assigned the input string, `letters` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `new_strings` contains the characters at the new indices for all characters in `strings` after applying the transformation described in the loop, `index` is the index of each character `s` in the string `letters`, `added_index` is the sum of `index` and `n` for each character, `new_index` is the remainder of `added_index` divided by 26 for each character, `new_s` is the character at the new index in the `letters` string for each character in `strings`
    print(new_strings)
#Overall this is what the function does:The function `func` reads an integer `n` from the user input, then reads a string `strings`. It performs a character transformation on each character in `strings` based on the value of `n` by shifting each character in the string `letters`. The transformed string is printed as output. The function does not accept any parameters and does not have any return value.

