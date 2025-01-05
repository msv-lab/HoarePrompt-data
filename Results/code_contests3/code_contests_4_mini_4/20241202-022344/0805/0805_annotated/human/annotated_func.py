#State of the program right berfore the function call: S is a string consisting of uppercase English letters, and N is an integer such that 0 <= N <= 26. The length of S is at least 1 and at most 10,000.
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
        
    #State of the program after the  for loop has been executed: `new_strings` is the string formed by shifting each character in `strings` by `n` positions in the alphabet; `S` is a string consisting of uppercase English letters, `N` is an integer such that 0 <= `N` <= 26, `n` is an input integer, `strings` is a string consisting of uppercase English letters, `letters` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
    print(new_strings)
#Overall this is what the function does:The function accepts an integer `n` (which is read from input) and a string `strings` (also read from input) consisting of uppercase English letters. It shifts each character in `strings` by `n` positions in the alphabet and wraps around if necessary, producing a new string. The function then prints the resultant shifted string. However, the function does not handle the case where the input `n` is out of the specified range (0 <= n <= 26), and if `n` is not provided as expected, the function will not behave correctly.

