#State of the program right berfore the function call: S is a string consisting of uppercase English letters, and N is an integer such that 0 <= N <= 26.
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
        
    #State of the program after the  for loop has been executed: `S` is a string consisting of uppercase English letters, `N` is an integer such that 0 <= `N` <= 26, `n` is an input integer, `strings` is a string, `letters` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `new_strings` is a string consisting of characters from `letters` shifted by `n` positions for each character in `strings`.
    print(new_strings)
#Overall this is what the function does:The function reads an integer `n` and a string of uppercase letters, shifts each letter in the string by `n` positions in the alphabet, and prints the transformed string. It does not validate inputs for ranges or letter cases and does not return any value.

