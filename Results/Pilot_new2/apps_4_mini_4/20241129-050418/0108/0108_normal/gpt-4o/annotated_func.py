#State of the program right berfore the function call: s is a string consisting of lowercase English letters with a length between 1 and 100,000.
def func():
    s = input()
    target = 'abcdefghijklmnopqrstuvwxyz'
    target_len = len(target)
    i, j = 0, 0
    while i < len(s) and j < target_len:
        if s[i] == target[j]:
            j += 1
        
        i += 1
        
    #State of the program after the loop has been executed: `i` is equal to the length of `s` if `s` contains all letters from 'a' to 'z' in order; `i` is less than the length of `s` if `s` does not contain all letters from 'a' to 'z' in order; `j` is equal to the number of characters from the beginning of `target` that were matched in sequence with `s`, which can be between 0 and 26; if `j` is less than 26, `len(s)` is greater than `i` and `j` is less than `target_len`.
    if (j == target_len) :
        print(target)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`i` is equal to the length of `s` if `s` contains all letters from 'a' to 'z' in order; `i` is less than the length of `s` if `s` does not contain all letters from 'a' to 'z' in order; `j` is equal to the number of characters from the beginning of `target` that were matched in sequence with `s`, which can be between 0 and 26; if `j` is equal to `target_len`, `target` is printed. Otherwise, if `j` is less than 26, `len(s)` is greater than `i`, and `j` is not equal to `target_len`, a value of -1 has been printed.
#Overall this is what the function does:The function accepts a string `s` which consists of lowercase English letters. It checks if `s` contains all letters from 'a' to 'z' in order, and if so, it prints the complete alphabet; otherwise, it prints -1. If `s` is missing any letters from 'a' to 'z' in the required sequence, the function indicates this by printing -1. The function does not return any value, and it operates on input read from the standard input.

