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
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `strings` is the input string, `letters` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `new_strings` is the result string after applying the transformation to each character in `strings` based on `n`
    print(new_strings)
#Overall this is what the function does:The function reads an integer `n` and a string `strings`, then applies a transformation to each character in `strings` based on the value of `n`. The transformed characters are concatenated to form a new string `new_strings`, which is then printed. The transformation involves shifting each character in `strings` by `n` positions in the alphabet, wrapping around if necessary.

