#State of the program right berfore the function call: N is an integer such that 0 <= N <= 26, and S is a string consisting of uppercase English letters with a length between 1 and 10,000.
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
        
    #State of the program after the  for loop has been executed: `new_strings` is the result of shifting each character in `strings` by `N` positions in the alphabet, and `strings` is unchanged.
    print(new_strings)
#Overall this is what the function does:The function accepts an integer `N` (where 0 <= N <= 26) and a string `S` consisting of uppercase English letters. It shifts each character in `S` by `N` positions in the alphabet, wrapping around if necessary, and outputs the resulting string. However, the function lacks input validation, meaning it assumes valid inputs will always be provided without handling potential input errors.

