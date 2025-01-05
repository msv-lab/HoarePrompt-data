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
        
    #State of the program after the  for loop has been executed: `new_strings` is the result of shifting each character in `strings` by `n` positions in the alphabet, `s` is the last character of `strings`, `N` is the length of `strings`, `letters` contains uppercase English letters.
    print(new_strings)
#Overall this is what the function does:The function accepts a string `strings` consisting of uppercase English letters and an integer `n` (where 0 <= n <= 26), then shifts each character in `strings` by `n` positions in the alphabet, wrapping around from 'Z' to 'A' as necessary. It prints the resulting transformed string. The function does not handle invalid input cases, such as if the input string contains characters outside the uppercase English letters or if `n` is outside the specified range.

