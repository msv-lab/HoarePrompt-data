#State of the program right berfore the function call: s is a string consisting of lowercase English letters.**
def func():
    s = input()
    target = 'abcdefghijklmnopqrstuvwxyz'
    target_len = len(target)
    i, j = 0, 0
    while i < len(s) and j < target_len:
        if s[i] == target[j]:
            j += 1
        
        i += 1
        
    #State of the program after the loop has been executed: `s` is a string consisting of lowercase English letters, `target` is the string 'abcdefghijklmnopqrstuvwxyz', `target_len` is the length of the string 'abcdefghijklmnopqrstuvwxyz', `i` is equal to len(s), `j` is equal to target_len
    if (j == target_len) :
        print(target)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`s` is a string consisting of lowercase English letters, `target` is the string 'abcdefghijklmnopqrstuvwxyz', `target_len` is the length of the string 'abcdefghijklmnopqrstuvwxyz', `i` is equal to len(s), `j` is equal to target_len. If j == target_len, then 'abcdefghijklmnopqrstuvwxyz' is printed. Otherwise, -1 is printed.
#Overall this is what the function does:The function `func` reads a string `s` of lowercase English letters from the user input. It then compares each character of `s` with the string 'abcdefghijklmnopqrstuvwxyz' character by character. If all characters match in order, the function prints 'abcdefghijklmnopqrstuvwxyz'. Otherwise, it prints -1. The function does not explicitly return any value.

