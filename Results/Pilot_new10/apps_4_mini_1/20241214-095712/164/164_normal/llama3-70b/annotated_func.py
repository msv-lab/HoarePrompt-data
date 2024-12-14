#State of the program right berfore the function call: n is an integer between 2 and 100, k is an integer between 1 and n-1, and the input string of length n contains exactly one 'G' and one 'T' character, with the remaining characters being either '.' or '#' (representing empty cells and obstacles, respectively).
def func():
    n, k = map(int, input().split())
    s = input()
    g, t = -1, -1
    for i in range(n):
        if s[i] == 'G':
            g = i
        elif s[i] == 'T':
            t = i
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 100, `g` is the index of the last occurrence of 'G' in the string `s` or -1 if 'G' does not occur, `t` is the index of the last occurrence of 'T' in the string `s` or -1 if 'T' does not occur, `s` is the input string.
    if (g == -1 or t == -1) :
        print('NO')
    else :
        if (abs(t - g) % k == 0 and all(s[(g + i * k) % n] != '#' for i in range(abs(t -
    g) // k + 1))) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is an integer between 2 and 100, `g` is the index of the last occurrence of 'G' in the string `s`, `t` is the index of the last occurrence of 'T' in the string `s`, both `g` and `t` are not equal to -1. If the absolute difference between `t` and `g` is divisible by `k` and all indices from `g` to `t` with a step of `k` contain elements in string `s` that are not equal to '#', the output 'YES' is printed. Otherwise, if the absolute difference between `t` and `g` is not divisible by `k`, or if there exists an index `i` such that `s[(g + i * k) % n]` is equal to '#' for some valid `i`, the output 'NO' is printed.
    #State of the program after the if-else block has been executed: *`n` is an integer between 2 and 100, `g` is the index of the last occurrence of 'G' in the string `s` or -1 if 'G' does not occur, `t` is the index of the last occurrence of 'T' in the string `s` or -1 if 'T' does not occur, `s` is the input string. If either `g` or `t` is -1, the string 'NO' has been printed. Otherwise, if both `g` and `t` are valid indices, the output 'YES' is printed if the absolute difference between `t` and `g` is divisible by `k` and all indices from `g` to `t` with a step of `k` contain elements in string `s` that are not equal to '#'. If the conditions for printing 'YES' are not met, the output 'NO' is printed.
#Overall this is what the function does:The function accepts two integers, `n` (between 2 and 100) and `k` (between 1 and n-1), along with a string of length `n` containing exactly one 'G' and one 'T' character, and characters representing empty cells or obstacles. It checks if it is possible to reach 'T' from 'G' by moving `k` steps at a time, ensuring that no obstacles ('#') are encountered along the way. If it is possible, it outputs 'YES'; otherwise, it outputs 'NO'. If either 'G' or 'T' is not found in the string, it outputs 'NO'.

