#State of the program right berfore the function call: N is an integer such that 0 <= N <= 26. S is a string consisting of uppercase English letters with a length between 1 and 10^4.**
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
        
    #State of the program after the  for loop has been executed: N is an integer between 0 and 26, S is a string, new_strings is a string consisting of characters from the `letters` list, where new_strings is the result of shifting each character in S by N positions in the `letters` list.
    print(new_strings)
#Overall this is what the function does:The function `func` reads an integer `N` and a string `S` from the user input. It then shifts each character in the string `S` by `N` positions in the alphabet (considering only uppercase English letters) and prints the resulting modified string. The function operates under the constraints that `N` is an integer between 0 and 26, and `S` is a string consisting of uppercase English letters with a length between 1 and 10^4. The function does not have an explicit return value.

