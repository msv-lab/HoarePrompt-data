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
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `strings` is assigned the input string, `letters` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `new_strings` contains characters from `letters` based on calculations in the loop for each character in `strings`
    print(new_strings)
#Overall this is what the function does:The function `func` takes user input for an integer `n` and a string `strings`. It then performs a Caesar cipher encryption on the input string by shifting each letter in the string by `n` positions. The function prints the encrypted string as the output. The functionality of the function does not involve any return value.

