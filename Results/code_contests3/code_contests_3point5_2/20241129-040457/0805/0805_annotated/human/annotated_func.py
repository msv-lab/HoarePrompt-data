#State of the program right berfore the function call: N is an integer such that 0 <= N <= 26. S is a string consisting of uppercase English letters with a length between 1 and 10^4.
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
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 0 <= N <= 26, `S` is a string consisting of uppercase English letters, `letters` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `new_strings` is a string consisting of characters from `letters` based on the calculations for each character in `S` after all iterations of the loop have finished.
    print(new_strings)
#Overall this is what the function does:The function `func` takes user input for an integer `n` and a string `strings` consisting of uppercase English letters. It then shifts each letter in `strings` by `n` positions in the alphabet, wrapping around if needed. The function prints the resulting string `new_strings`. The function does not explicitly return any value.

