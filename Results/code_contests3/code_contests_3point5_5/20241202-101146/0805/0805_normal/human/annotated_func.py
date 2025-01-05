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
        
    #State of the program after the  for loop has been executed: `new_strings` contains the updated characters based on the formula for all elements in `strings`, `index` is the index of the last character in `strings` in the list `letters`, `added_index` is the result of `index + n` for the last character in `strings`, `new_index` is the result of `added_index % 26` for the last character in `strings`, `new_s` is assigned the value based on the calculation for the last character in `strings`
    print(new_strings)
#Overall this is what the function does:The function reads an integer `n` and a string of uppercase letters. It then shifts each letter in the string by `n` positions to the right in the alphabet (wrapping around if needed) and prints the resulting modified string.

