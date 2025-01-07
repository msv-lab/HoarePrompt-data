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
        
    #State of the program after the loop has been executed: Output State: `s` is assigned the input string provided by the user, `target` is the string 'abcdefghijklmnopqrstuvwxyz', `target_len` is 26, `i` may be equal to or greater than the length of string `s`, `j` may be equal to or greater than 26, both `i` and `j` have been incremented accordingly based on the condition `s[i] == target[j]`.
    if (j == target_len) :
        print(target)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`s` is assigned the input string provided by the user, `target` is the string 'abcdefghijklmnopqrstuvwxyz', `target_len` is 26, `i` may be equal to or greater than the length of string `s`, `j` may be equal to or greater than 26, both `i` and `j` have been incremented accordingly based on the condition `s[i] == target[j]`. If `j` equals `target_len`, the program has processed all elements of `target`. Otherwise, `j` does not equal `target_len` and no variables are affected by the code snippet `print(-1)`.
#Overall this is what the function does:The function reads a string s consisting of lowercase English letters from the user. It then iterates through the string s and the string 'abcdefghijklmnopqrstuvwxyz' simultaneously, trying to match characters. If it successfully matches all characters in 'abcdefghijklmnopqrstuvwxyz' with s, it prints 'abcdefghijklmnopqrstuvwxyz'. Otherwise, it prints -1. The function does not explicitly return any value.

