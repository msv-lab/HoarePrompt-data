#State of the program right berfore the function call: S is a string consisting of uppercase English letters, and N is an integer such that 0 <= N <= 26. The length of S is between 1 and 10^4.
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
        
    #State of the program after the  for loop has been executed: `S` is a string consisting of uppercase English letters, `N` is an integer such that 0 <= `N` <= 26, `n` is an input integer, `strings` is a string with at least one character, `letters` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `new_strings` is the result of shifting each character in `strings` by `n` positions in the alphabet, wrapping around if necessary.
    print(new_strings)
#Overall this is what the function does:The function accepts a string `S` consisting of uppercase English letters and an integer `N` (0 <= N <= 26) from user input, then shifts each character in `S` forward by `N` positions in the alphabet, wrapping around if necessary. The function outputs the transformed string based on these shifts. However, it does not handle invalid input cases such as non-uppercase letters or invalid integer values for `N`.

