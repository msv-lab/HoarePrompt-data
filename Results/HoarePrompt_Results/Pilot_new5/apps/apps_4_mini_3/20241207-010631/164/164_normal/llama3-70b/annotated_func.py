#State of the program right berfore the function call: n is an integer between 2 and 100 (inclusive), k is an integer between 1 and n-1 (inclusive), and the input string of length n consists of characters '.', '#', 'G', and 'T' such that 'G' and 'T' appear exactly once.
def func():
    n, k = map(int, input().split())
    s = input()
    g, t = -1, -1
    for i in range(n):
        if s[i] == 'G':
            g = i
        elif s[i] == 'T':
            t = i
        
    #State of the program after the  for loop has been executed: `n` is between 2 and 100, `k` is between 1 and `n-1`, `s` is an input string, `g` is the index of the last occurrence of 'G' in `s` or -1 if 'G' is not present, `t` is the index of the last occurrence of 'T' in `s` or -1 if 'T' is not present.
    if (g == -1 or t == -1) :
        print('NO')
    else :
        if (abs(t - g) % k == 0 and all(s[(g + i * k) % n] != '#' for i in range(abs(t -
    g) // k + 1))) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is between 2 and 100, `k` is between 1 and `n-1`, `s` is an input string, `g` is the index of the last occurrence of 'G' in `s`, which is not -1, and `t` is the index of the last occurrence of 'T' in `s`, which is not -1. If the absolute difference between `t` and `g` is divisible by `k` and all characters at indices `(g + i * k) % n` in `s` are not '#', then 'YES' is printed. Otherwise, if the absolute difference is not divisible by `k`, or there exists an integer `i` such that `s[(g + i * k) % n]` equals '#', then 'NO' is printed.
    #State of the program after the if-else block has been executed: *`n` is between 2 and 100, `k` is between 1 and `n-1`, `s` is an input string. If either `g` (the index of the last occurrence of 'G' in `s`) or `t` (the index of the last occurrence of 'T' in `s`) is -1, the output is 'NO'. Otherwise, if `g` and `t` are not -1, and the absolute difference between `t` and `g` is divisible by `k`, and all characters at indices `(g + i * k) % n` in `s` are not '#', then 'YES' is printed. If either the absolute difference is not divisible by `k`, or there exists an integer `i` such that `s[(g + i * k) % n]` equals '#', then 'NO' is printed.
#Overall this is what the function does:The function accepts two integers `n` (between 2 and 100 inclusive) and `k` (between 1 and `n-1` inclusive), along with a string `s` of length `n` that contains characters '.', '#', 'G', and 'T' (with 'G' and 'T' appearing exactly once). It checks if it's possible to reach the character 'T' starting from 'G' by moving in increments of `k` positions in the string, wrapping around if necessary, and ensuring there are no '#' characters in the path. If the conditions are met, it prints 'YES'; otherwise, it prints 'NO'. If either 'G' or 'T' is not found in the string, it prints 'NO'.

