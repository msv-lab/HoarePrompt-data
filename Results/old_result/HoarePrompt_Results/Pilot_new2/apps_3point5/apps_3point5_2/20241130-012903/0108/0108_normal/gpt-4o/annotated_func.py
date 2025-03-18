#State of the program right berfore the function call: **Precondition**: s is a string consisting of lowercase English letters.
def func():
    s = input()
    target = 'abcdefghijklmnopqrstuvwxyz'
    target_len = len(target)
    i, j = 0, 0
    while i < len(s) and j < target_len:
        if s[i] == target[j]:
            j += 1
        
        i += 1
        
    #State of the program after the loop has been executed: `s` is a string consisting of lowercase English letters, `target` is 'abcdefghijklmnopqrstuvwxyz', `target_len` is the length of target, `i` is equal to the length of `s`, `j` is equal to the length of `target` if all characters of `target` were found in `s`, else `j` is less than the length of `target`
    if (j == target_len) :
        print(target)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`s` is a string consisting of lowercase English letters, `target` is 'abcdefghijklmnopqrstuvwxyz', `target_len` is the length of target, `i` is equal to the length of `s`, `j` is equal to the length of `target` if all characters of `target` were found in `s`, else `j` is less than the length of `target`. If `j` is equal to `target_len`, the string 'abcdefghijklmnopqrstuvwxyz' is printed. Otherwise, if `j` is not equal to `target_len`, -1 is printed.
#Overall this is what the function does:The function `func` reads a string `s` from user input and iterates through it to find the characters of the target string 'abcdefghijklmnopqrstuvwxyz' in the same order. If all characters are found in `s`, it prints 'abcdefghijklmnopqrstuvwxyz'. If not, it prints -1. The function does not accept any parameters and has no specified return value.

