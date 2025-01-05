#State of the program right berfore the function call: S is a string consisting of uppercase English letters, and N is a non-negative integer such that 0 <= N <= 26. The length of S is between 1 and 10^4.
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
        
    #State of the program after the  for loop has been executed: `S` is a string consisting of uppercase English letters, `N` is a non-negative integer such that 0 <= `N` <= 26, `n` is an input integer, `strings` is a string consisting of uppercase English letters, `letters` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `new_strings` is the result of each character in `strings` shifted by `n` positions in `letters`.
    print(new_strings)
#Overall this is what the function does:The function accepts a non-negative integer `n` and a string `strings` consisting of uppercase English letters. It shifts each character in `strings` by `n` positions in the alphabet, wrapping around if necessary. The output is the transformed string where each character is replaced by the character that is `n` positions further along in the alphabet. If `n` is 0, the output will be the same as the input string. The function does not take parameters directly; instead, it reads them from user input.

