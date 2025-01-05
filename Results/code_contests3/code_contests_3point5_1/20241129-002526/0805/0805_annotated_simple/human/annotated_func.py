#State of the program right berfore the function call: N is an integer such that 0 <= N <= 26. S is a string consisting of uppercase English letters with length between 1 and 10^4.**
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
        
    #State of the program after the  for loop has been executed: `new_strings` will be a string consisting of the letters in the `letters` list shifted by `N` positions based on the input `S` string. The `new_index` will be the index of the last letter shifted in the `letters` list.
    print(new_strings)
#Overall this is what the function does:The function `func` reads an integer `N` and a string `S` as input. It then shifts each letter in the `S` string by `N` positions in the alphabet (wrapping around if necessary) and prints the resulting string `new_strings`. The function does not explicitly return any value. However, there is a missing functionality in the annotations regarding error handling if `N` is not within the specified range or if `S` contains characters other than uppercase English letters.

