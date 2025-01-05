#State of the program right berfore the function call: S is a string consisting of uppercase English letters, and N is a non-negative integer such that 0 <= N <= 26. The length of S is between 1 and 10,000.
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
        
    #State of the program after the  for loop has been executed: `S` is a string consisting of uppercase English letters, `N` is a non-negative integer such that 0 <= `N` <= 26, `n` is an input integer, `strings` is a string consisting of uppercase English letters, `new_strings` is a string formed by shifting each character in `strings` by `n` positions in the alphabet, wrapping around if necessary.
    print(new_strings)
#Overall this is what the function does:The function accepts a string `S` consisting of uppercase English letters and an integer `N` that is read from input (0 <= N <= 26). It shifts each letter in the string `S` by `N` positions in the alphabet, wrapping around if necessary, and outputs the resulting string. The function does not explicitly return any value; it only prints the transformed string.

