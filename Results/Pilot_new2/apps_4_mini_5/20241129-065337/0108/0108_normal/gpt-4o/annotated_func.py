#State of the program right berfore the function call: s is a string consisting of lowercase English letters with a length between 1 and 100,000 inclusive.
def func():
    s = input()
    target = 'abcdefghijklmnopqrstuvwxyz'
    target_len = len(target)
    i, j = 0, 0
    while i < len(s) and j < target_len:
        if s[i] == target[j]:
            j += 1
        
        i += 1
        
    #State of the program after the loop has been executed: `i` is equal to the length of `s`, `j` is less than or equal to `target_len` (26), if `j` is equal to `target_len`, then `s` contains all the letters from `target` in order; if `j` is less than `target_len`, then `s` does not contain all letters from `target` in order.
    if (j == target_len) :
        print(target)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`i` is equal to the length of `s`, `j` is less than or equal to `target_len` (26). If `j` is equal to `target_len`, then `s` contains all the letters from `target` in order, and `target` is printed. Otherwise, if `j` is less than `target_len`, `-1` is printed.
#Overall this is what the function does:The function accepts a string `s` of lowercase English letters and outputs 'abcdefghijklmnopqrstuvwxyz' if `s` contains all letters from 'a' to 'z' in order; otherwise, it prints -1.

