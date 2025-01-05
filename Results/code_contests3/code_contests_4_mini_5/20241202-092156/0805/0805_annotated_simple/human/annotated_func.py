#State of the program right berfore the function call: S is a string consisting of uppercase English letters, and N is an integer such that 0 <= N <= 26. The length of S is between 1 and 10,000 characters.
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
        
    #State of the program after the  for loop has been executed: `S` is a string consisting of uppercase English letters, `N` is an integer such that 0 <= N <= 26, `n` is an input integer, `strings` is a string of length at least 0, `letters` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `new_strings` is the result of shifting each character in `strings` by `n` positions in the alphabet, where each character wraps around after 'Z' if necessary.
    print(new_strings)
#Overall this is what the function does:The function accepts an integer `n` and a string `S` of uppercase English letters. It shifts each letter in `S` by `n` positions in the English alphabet, wrapping around after 'Z' if necessary, and outputs the resulting string. The function does not handle cases where the input string is empty or where the integer input is out of the specified bounds.

