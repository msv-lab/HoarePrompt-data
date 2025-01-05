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
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `strings` is a string, `letters` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `new_strings` contains the characters at the new indices in `letters` for each character in `strings`.
    print(new_strings)
#Overall this is what the function does:The function takes an integer input `n` and a string `strings`, shifts each character in `strings` by `n` positions in the alphabet (wrapping around if needed), and prints the resulting string `new_strings`. The function does not return any value.

