#State of the program right berfore the function call: **Precondition**: **s is a string consisting of |s| small English letters where 1 ≤ |s| ≤ 10^5.**
def func():
    s = input()
    target = 'abcdefghijklmnopqrstuvwxyz'
    target_len = len(target)
    i, j = 0, 0
    while i < len(s) and j < target_len:
        if s[i] == target[j]:
            j += 1
        
        i += 1
        
    #State of the program after the loop has been executed: `s` is a string consisting of |s| small English letters where 1 ≤ |s| ≤ 10^5, `target` is the string 'abcdefghijklmnopqrstuvwxyz', `target_len` is the length of the string 'abcdefghijklmnopqrstuvwxyz', `i` is equal to len(s), `j` is equal to target_len or less
    if (j == target_len) :
        print(target)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`s` is a string consisting of |s| small English letters where 1 ≤ |s| ≤ 10^5, `target` is the string 'abcdefghijklmnopqrstuvwxyz', `target_len` is the length of the string 'abcdefghijklmnopqrstuvwxyz', `i` is equal to len(s), `j` is equal to target_len or less. If j is equal to target_len, then `target` is printed out. If j is less than target_len, the program continues with the updated values of the variables.
#Overall this is what the function does:Functionality: The function `func` does not accept any parameters. It reads a string `s` from the user, and it iterates over `s` and the string 'abcdefghijklmnopqrstuvwxyz' to match characters. If the characters in `s` match the sequence in 'abcdefghijklmnopqrstuvwxyz' consecutively, it prints 'abcdefghijklmnopqrstuvwxyz'. Otherwise, it prints -1. The functionality of the function is to check if the input string `s` contains the sequence 'abcdefghijklmnopqrstuvwxyz' in order. If it does, the function prints 'abcdefghijklmnopqrstuvwxyz'; otherwise, it prints -1.

