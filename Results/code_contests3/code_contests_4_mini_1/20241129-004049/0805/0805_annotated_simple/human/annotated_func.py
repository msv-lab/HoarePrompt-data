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
        
    #State of the program after the  for loop has been executed: `new_strings` is the result of shifting each character in `strings` by `n` positions in the alphabet, `S` is a string consisting of uppercase English letters, `N` is an integer such that 0 <= `N` <= 26, `n` is an input integer, `strings` is the original input string.
    print(new_strings)
#Overall this is what the function does:The function accepts an integer `n` and a string `strings` consisting of uppercase English letters. It shifts each letter in `strings` by `n` positions in the alphabet, wrapping around if necessary (e.g., shifting 'Z' by 1 will result in 'A'). The function does not validate the input for `n`, and it assumes the user will provide a valid integer within the range 0 to 26. It then prints the resulting shifted string.

