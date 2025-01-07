#State of the program right berfore the function call: s is a string consisting of lowercase English letters with length between 1 and 100,000.
def func():
    s = input()
    target = 'abcdefghijklmnopqrstuvwxyz'
    target_len = len(target)
    i, j = 0, 0
    while i < len(s) and j < target_len:
        if s[i] == target[j]:
            j += 1
        
        i += 1
        
    #State of the program after the loop has been executed: `i` is equal to the length of `s`, `j` is equal to the number of characters from `target` that were found in `s` in order, which is between 0 and 26. If `j` is less than 26, then not all characters of `target` were found in `s`. If `j` is 26, then all characters of `target` were found in `s` in order.
    if (j == target_len) :
        print(target)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`i` is equal to the length of `s`. If `j` is equal to `target_len`, then all characters of `target` were found in `s` in order, and `target` is printed. Otherwise, `j` is between 0 and 25, indicating that not all characters of `target` were found in `s` in order.
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase English letters and checks if all the letters of the English alphabet (from 'a' to 'z') are present in `s` in order. If all characters are found in the correct order, it prints the alphabet; otherwise, it prints -1. This means if `s` is missing any characters from the alphabet or if they are not in the correct order, the function will return -1.

