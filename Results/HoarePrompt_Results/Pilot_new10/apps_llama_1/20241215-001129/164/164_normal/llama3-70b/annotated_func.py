#State of the program right berfore the function call: The input consists of two lines. The first line contains two integers n and k, where n is a positive integer from 2 to 100, and k is a positive integer from 1 to n-1. The second line is a string of length n consisting of characters '.', '#', 'G', and 'T', where 'G' and 'T' appear exactly once.
def func():
    n, k = map(int, input().split())
    s = input()
    g, t = -1, -1
    for i in range(n):
        if s[i] == 'G':
            g = i
        elif s[i] == 'T':
            t = i
        
    #State of the program after the  for loop has been executed: `n` is a positive integer from 2 to 100, `k` is a positive integer from 1 to `n-1`, `s` is a string of length `n` consisting of characters '.', '#', 'G', and 'T', where 'G' and 'T' appear exactly once, `g` is the index of 'G' in `s`, `t` is the index of 'T' in `s`.
    if (g == -1 or t == -1) :
        print('NO')
    else :
        if (abs(t - g) % k == 0 and all(s[(g + i * k) % n] != '#' for i in range(abs(t -
    g) // k + 1))) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: `n` is a positive integer from 2 to 100, `k` is a positive integer from 1 to `n-1`, `s` is a string of length `n` consisting of characters '.', '#', 'G', and 'T', where 'G' and 'T' appear exactly once, `g` is the index of 'G' in `s`, `t` is the index of 'T' in `s`, and both `g` and `t` are not equal to -1. If the absolute difference between `t` and `g` is a multiple of `k` and the substring of `s` from `g` to `t` (or `t` to `g`), stepping by `k`, contains no '#' characters, then 'YES' has been printed. Otherwise, 'NO' has been printed.
    #State of the program after the if-else block has been executed: *`n` is a positive integer from 2 to 100, `k` is a positive integer from 1 to `n-1`, `s` is a string of length `n` consisting of characters '.', '#', 'G', and 'T`. If 'G' or 'T' is not found in `s`, 'NO' has been printed to the console. Otherwise, `g` is the index of 'G' in `s` and `t` is the index of 'T' in `s`, and if the absolute difference between `t` and `g` is a multiple of `k` and the substring of `s` from `g` to `t` (or `t` to `g`), stepping by `k`, contains no '#' characters, then 'YES' has been printed. In all other cases, 'NO' has been printed.
#Overall this is what the function does:The function reads two lines of input, the first line containing two positive integers `n` and `k`, and the second line a string of length `n` with specific characters, and it prints 'YES' if the absolute difference between the indices of 'G' and 'T' is a multiple of `k` and the substring of `s` from `g` to `t` (or `t` to `g`), stepping by `k`, contains no '#' characters; otherwise, it prints 'NO', assuming the input is well-formed and 'G' and 'T' appear exactly once in the string.

