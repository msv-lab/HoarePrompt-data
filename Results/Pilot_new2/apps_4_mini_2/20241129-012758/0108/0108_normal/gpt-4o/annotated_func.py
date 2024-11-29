#State of the program right berfore the function call: s is a string consisting of lowercase English letters with a length between 1 and 100,000 (1 ≤ |s| ≤ 10^5).
def func():
    s = input()
    target = 'abcdefghijklmnopqrstuvwxyz'
    target_len = len(target)
    i, j = 0, 0
    while i < len(s) and j < target_len:
        if s[i] == target[j]:
            j += 1
        
        i += 1
        
    #State of the program after the loop has been executed: `i` is equal to `len(s)`; if `j` is equal to 26, then all characters of `target` were found in `s` in order; if `j` is less than 26, then not all characters of `target` were found in `s`.
    if (j == target_len) :
        print(target)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`i` is equal to `len(s)`; if `j` is equal to `target_len`, then all characters of `target` were found in `s` in order and `target` is printed. Otherwise, if `j` is less than `target_len`, then not all characters of `target` were found in `s`, and the output is -1.
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase English letters and checks whether it contains all the letters of the English alphabet ('a' to 'z') in order. If all letters are found in order, it prints the entire alphabet; otherwise, it prints -1. If the input string has a length of 1 or does not contain all 26 letters in the correct order, the function will print -1.

