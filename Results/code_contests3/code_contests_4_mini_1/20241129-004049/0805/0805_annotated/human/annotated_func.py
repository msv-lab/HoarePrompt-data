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
        
    #State of the program after the  for loop has been executed: `S` is a string consisting of uppercase English letters, `N` is a non-negative integer such that 0 <= `N` <= 26, `strings` is the input string, `new_strings` is the transformed string resulting from shifting each character of `strings` by `n` positions in the `letters` string.
    print(new_strings)
#Overall this is what the function does:The function accepts a non-negative integer `n` and a string `strings` consisting of uppercase English letters. It shifts each character in `strings` by `n` positions in the alphabet, wrapping around if necessary, and prints the resulting transformed string. The function does not return any value; instead, it outputs the transformed string directly.

