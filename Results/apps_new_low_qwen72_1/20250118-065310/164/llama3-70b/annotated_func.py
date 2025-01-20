#State of the program right berfore the function call: n and k are integers such that 2 ≤ n ≤ 100 and 1 ≤ k ≤ n - 1; the second argument is a string of length n consisting of characters '.', '#', 'G', and 'T', where 'G' and 'T' each appear exactly once.
def func():
    n, k = map(int, input().split())

s = input()

g, t = -1, -1
    for i in range(n):
        if s[i] == 'G':
            g = i
        elif s[i] == 'T':
            t = i
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 100 inclusive, `k` is an integer between 1 and `n-1` inclusive, `s` is a string of length `n` consisting of characters '.', '#', 'G', and 'T' where 'G' and 'T' each appear exactly once, `g` is the index of the character 'G' in `s`, `t` is the index of the character 'T' in `s`. The loop will always execute `n` times, and `i` will be `n-1` after the loop completes.
    if (g == -1 or t == -1) :
        print('NO')
    else :
        if (abs(t - g) % k == 0 and all(s[(g + i * k) % n] != '#' for i in range(abs(t -
    g) // k + 1))) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is an integer between 2 and 100 inclusive, `k` is an integer between 1 and `n-1` inclusive, `s` is a string of length `n` consisting of characters '.', '#', 'G', and 'T' where 'G' and 'T' each appear exactly once, `g` is the index of the character 'G' in `s`, `t` is the index of the character 'T' in `s`, `i` is `n-1` after the loop completes, `g` is not -1, `t` is not -1. If the absolute difference between `t` and `g` is divisible by `k` and for every step of size `k` from `g` to `t` (inclusive), the character at the corresponding position in `s` is not '#', 'YES' has been printed. Otherwise, either the absolute difference between `t` and `g` is not divisible by `k`, or there exists at least one index `i` in the range from 0 to `abs(t - g) // k + 1` such that `s[(g + i * k) % n]` is equal to '#'.
    #State of the program after the if-else block has been executed: *`n` is an integer between 2 and 100 inclusive, `k` is an integer between 1 and `n-1` inclusive, `s` is a string of length `n` consisting of characters '.', '#', 'G', and 'T' where 'G' and 'T' each appear exactly once, `g` is the index of the character 'G' in `s`, `t` is the index of the character 'T' in `s`, and `i` is `n-1` after the loop completes. If either `g` is -1 or `t` is -1, it indicates that at least one of the characters 'G' or 'T' is not found in the string `s`. Otherwise, `g` and `t` are valid indices. If the absolute difference between `t` and `g` is divisible by `k` and for every step of size `k` from `g` to `t` (inclusive), the character at the corresponding position in `s` is not '#', 'YES' has been printed. Otherwise, either the absolute difference between `t` and `g` is not divisible by `k`, or there exists at least one index `i` in the range from 0 to `abs(t - g) // k + 1` such that `s[(g + i * k) % n]` is equal to '#'.
#Overall this is what the function does:The function `func` takes no explicit parameters but reads two integers `n` and `k` from the standard input, followed by a string `s` of length `n` consisting of characters '.', '#', 'G', and 'T', where 'G' and 'T' each appear exactly once. It determines whether it is possible to move from the position of 'G' to the position of 'T' in the string `s` by making jumps of size `k` without landing on any '#' character. If such a path exists, the function prints 'YES'; otherwise, it prints 'NO'. The function does not return any value. The function ensures that `n` is an integer between 2 and 100 inclusive, `k` is an integer between 1 and `n-1` inclusive, and `s` is a valid string as described. Edge cases include scenarios where 'G' or 'T' are not found in the string, which would result in 'NO' being printed.

