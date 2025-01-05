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
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `strings` is a non-empty string, `letters` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `new_strings` contains the characters based on the calculations from all the iterations of the loop, `s` is the last character in `strings`, `index` is the index of the last character, `added_index` is the sum of `index` and `n` for the last character, `new_index` is the remainder of `added_index` divided by 26 for the last character, `new_s` is a character from the 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' string based on `new_index`.
    print(new_strings)
#Overall this is what the function does:The function prompts the user for an integer `n` and a non-empty string `strings`, then performs a Caesar cipher encryption on the input string based on the value of `n`. It shifts each letter in the input string by `n` positions in the alphabet and prints the resulting encrypted string. The function does not accept any parameters and only operates based on user input.

