#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 100, k is an integer such that 1 ≤ k ≤ n - 1, and the line is represented as a string of length n containing exactly one 'G' and one 'T', with remaining characters being '.' (empty cells) or '#' (obstacles).
def func():
    n, k = map(int, input().split())
    s = input()
    g, t = -1, -1
    for i in range(n):
        if s[i] == 'G':
            g = i
        elif s[i] == 'T':
            t = i
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 100, `k` is an integer such that 1 ≤ `k` ≤ `n - 1`, `s` is an input string, `g` is the index of the last occurrence of 'G' in `s`, or -1 if 'G' did not occur, `t` is the index of the last occurrence of 'T' in `s`, or -1 if 'T' did not occur.
    if (g == -1 or t == -1) :
        print('NO')
    else :
        if (abs(t - g) % k == 0 and all(s[(g + i * k) % n] != '#' for i in range(abs(t -
    g) // k + 1))) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is an integer such that 2 ≤ `n` ≤ 100, `k` is an integer such that 1 ≤ `k` ≤ `n - 1`, `s` is an input string, `g` is the index of the last occurrence of 'G' in `s` which is not -1, `t` is the index of the last occurrence of 'T' in `s` which is not -1. If the absolute difference between `t` and `g` is divisible by `k`, and all characters at the positions `(g + i * k) % n` in `s` for `i` from 0 to `abs(t - g) // k` are not '#', then 'YES' has been printed. Otherwise, 'NO' has been printed.
    #State of the program after the if-else block has been executed: *`n` is an integer such that 2 ≤ `n` ≤ 100, `k` is an integer such that 1 ≤ `k` ≤ `n - 1`, `s` is an input string. If either `g` or `t` is -1, the output is 'NO'. If both `g` and `t` are valid indices (not -1), and the absolute difference between `t` and `g` is divisible by `k`, and all characters at the positions `(g + i * k) % n` for `i` from 0 to `abs(t - g) // k` in `s` are not '#', then 'YES' is printed; otherwise, 'NO' is printed.
#Overall this is what the function does:The function takes two integers, `n` and `k`, and a string `s`. It checks if there is a valid path from the position of 'G' to 'T' in the string while adhering to the following conditions: the distance between 'G' and 'T' must be divisible by `k`, and all positions along this path must not contain obstacles ('#'). If either 'G' or 'T' is missing, or if the path conditions are not met, it prints 'NO'. If the conditions are satisfied, it prints 'YES'. The final state of the program is indicated by either 'YES' or 'NO' being printed, depending on the feasibility of the path. The potential edge cases include scenarios where 'G' and 'T' are not found in the input string or where characters between them are obstacles regardless of distance.

