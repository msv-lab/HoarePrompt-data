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
        
    #State of the program after the loop has been executed: s` is a string consisting of lowercase English letters, `target` is 'abcdefghijklmnopqrstuvwxyz', `target_len` is 26, `i` must be equal to the length of `s`, `j` must be 26 or less, and if `s[i]` is equal to `target[j]`, then `j` is 26, `i` is incremented by 1 until `i` is equal to the length of `s`
    if (j == target_len) :
        print(target)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`s` is a string consisting of lowercase English letters, `target` is 'abcdefghijklmnopqrstuvwxyz', `target_len` is 26, `i` is equal to the length of `s`, `j` is either 26 or less. If `j` is 26, then `s[i]` is equal to `target[j]`. If `j` is less than 26 and `s[i]` is equal to `target[j]`, then `j` is not equal to 26. `i` is incremented by 1 until `i` is equal to the length of `s`.
#Overall this is what the function does:Functionality: The function `func` reads a string `s` input consisting of lowercase English letters and compares it with the target string 'abcdefghijklmnopqrstuvwxyz'. It iterates through `s` and 'abcdefghijklmnopqrstuvwxyz' character by character, and if all characters in `s` match the corresponding characters in the target string, it prints 'abcdefghijklmnopqrstuvwxyz'. If there is no match, it prints -1. The function does not accept any parameters and does not return any value.

