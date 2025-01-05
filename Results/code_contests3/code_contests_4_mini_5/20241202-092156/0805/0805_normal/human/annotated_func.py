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
        
    #State of the program after the  for loop has been executed: `S` is a string consisting of uppercase English letters; `N` is an integer such that 0 <= N <= 26; `n` is an input integer; `strings` is an empty string; `letters` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'; `new_strings` is the string formed by applying the transformation to each letter in `strings` based on the integer `n`.
    print(new_strings)
#Overall this is what the function does:The function accepts an integer `n` and a string `strings` consisting of uppercase English letters. It shifts each letter in `strings` by `n` positions forward in the alphabet, wrapping around to the beginning after 'Z'. The transformed string is printed but not returned. The function does not handle the case of invalid inputs or provide any return values.

