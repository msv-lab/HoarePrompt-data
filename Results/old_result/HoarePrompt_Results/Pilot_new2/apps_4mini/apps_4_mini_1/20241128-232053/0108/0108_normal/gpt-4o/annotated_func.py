#State of the program right berfore the function call: s is a string consisting of 1 to 100,000 lowercase English letters.
def func():
    s = input()
    target = 'abcdefghijklmnopqrstuvwxyz'
    target_len = len(target)
    i, j = 0, 0
    while i < len(s) and j < target_len:
        if s[i] == target[j]:
            j += 1
        
        i += 1
        
    #State of the program after the loop has been executed: `i` is equal to the length of `s`, `j` is equal to the number of characters from `target` that were found in `s` in order (which can be between 0 and 26), and if `j` is less than 26 then `s` does not contain all characters of `target` in the required order; if `j` is equal to 26, then `s` contains all characters of `target` in order.
    if (j == target_len) :
        print(target)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`i` is equal to the length of `s`. If `j` is equal to the length of `target`, `target` is printed. Otherwise, if `j` is less than 26, the output is -1, indicating that not all characters of `target` were found in `s` in the required order.
#Overall this is what the function does:The function accepts a string `s` consisting of 1 to 100,000 lowercase English letters. It checks whether all characters of the English alphabet (from 'a' to 'z') appear in `s` in the correct order. If all characters are present, it prints the complete alphabet; otherwise, it prints -1. The function does not return any values; it only prints to the console.

