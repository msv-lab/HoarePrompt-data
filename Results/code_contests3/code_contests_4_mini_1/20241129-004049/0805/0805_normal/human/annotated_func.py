#State of the program right berfore the function call: S is a string consisting of uppercase English letters, and N is a non-negative integer such that 0 <= N <= 26.
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
        
    #State of the program after the  for loop has been executed: `S` is a string consisting of uppercase English letters formed by shifting each character in `strings` by `n` positions in the alphabet, `N` is a non-negative integer (0 <= `N` <= 26), `n` is an input integer, `strings` is a string consisting of uppercase English letters, `new_strings` is the transformed string after applying the shift to all characters in `strings`.
    print(new_strings)
#Overall this is what the function does:The function accepts a non-negative integer `n` and a string `strings` consisting of uppercase English letters. It transforms each letter in `strings` by shifting it `n` positions forward in the alphabet, wrapping around if necessary. The transformed string is then printed. However, the function does not handle cases where the input for `n` is not within the specified range (0 to 26), nor does it validate the input string for characters outside the uppercase English letters.

