#State of the program right berfore the function call: N is an integer such that 0 <= N <= 26 and S is a string consisting of uppercase English letters with length between 1 and 10^4.
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
        
    #State of the program after the  for loop has been executed: `new_strings` contains the characters from the `letters` list that are shifted by `n` positions in a circular manner
    print(new_strings)
#Overall this is what the function does:The function `func` reads an integer `n` and a string `strings`. It shifts each character in `strings` by `n` positions in a circular manner based on the uppercase English letters. The function then prints the modified string `new_strings`. The function does not explicitly return a value. It operates on the input parameters `n` and `strings` as described.

