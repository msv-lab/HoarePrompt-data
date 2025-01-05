#State of the program right berfore the function call: N is a non-negative integer such that 0 <= N <= 26, and S is a string consisting of uppercase English letters with a length between 1 and 10^4.
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
        
    #State of the program after the  for loop has been executed: `N` is a non-negative integer such that 0 <= `N` <= 26; `S` is a string consisting of uppercase English letters; `strings` is a string consisting of uppercase English letters with a length between 1 and 10^4; `new_strings` is a string that is the result of shifting each character in `strings` by `n` positions in the alphabet, wrapping around if necessary.
    print(new_strings)
#Overall this is what the function does:The function accepts a non-negative integer `N` (0 <= N <= 26) and a string `S` consisting of uppercase English letters (length between 1 and 10,000). It shifts each character in the string `S` by `N` positions in the alphabet, wrapping around if necessary, and outputs the resulting string.

