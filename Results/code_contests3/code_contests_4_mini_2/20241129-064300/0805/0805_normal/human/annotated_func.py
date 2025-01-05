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
        
    #State of the program after the  for loop has been executed: `S` is a string, `N` is an integer such that 0 <= `N` <= 26, `n` is an input integer, `strings` is a string, `letters` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `new_strings` is the string formed by shifting each character in `strings` by `n`.
    print(new_strings)
#Overall this is what the function does:The function accepts an integer input `n` and a string `strings` consisting of uppercase English letters. It transforms `strings` by shifting each character forward in the alphabet by `n` positions, wrapping around to the beginning of the alphabet if necessary. The transformed string is then printed. The function does not handle invalid inputs such as non-integer values for `n` or characters in `strings` that are not uppercase English letters, and it also does not limit the value of `n` to be within the specified range of 0 to 26, which may lead to unexpected behavior.

