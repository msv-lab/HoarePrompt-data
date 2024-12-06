#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 100, k is an integer such that 1 ≤ k ≤ n - 1, and the input string of length n contains exactly one 'G' and one 'T', along with any combination of '.' and '#', where '.' represents empty cells and '#' represents obstacles.
def func():
    n, k = map(int, input().split())
    s = input()
    g, t = -1, -1
    for i in range(n):
        if s[i] == 'G':
            g = i
        elif s[i] == 'T':
            t = i
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 100; `k` is an integer such that 1 ≤ `k` ≤ `n` - 1; `g` is the index of the last occurrence of 'G' in string `s` or remains -1 if 'G' does not exist; `t` is the index of the last occurrence of 'T' in string `s` or remains -1 if 'T' does not exist.
    if (g == -1 or t == -1) :
        print('NO')
    else :
        if (abs(t - g) % k == 0 and all(s[(g + i * k) % n] != '#' for i in range(abs(t -
    g) // k + 1))) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is an integer such that 2 ≤ `n` ≤ 100; `k` is an integer such that 1 ≤ `k` ≤ `n` - 1; `g` is the index of the last occurrence of 'G' in string `s`, such that `g` is not -1; `t` is the index of the last occurrence of 'T' in string `s`, such that `t` is not -1; if the absolute difference between `t` and `g` is divisible by `k` and for every `i` in the range from 0 to (abs(t - g) // k), the character at the index `(g + i * k) % n` in string `s` is not '#', then "YES" has been printed. Otherwise, if the absolute difference `abs(t - g)` is not divisible by `k`, or there exists at least one index `i` such that `s[(g + i * k) % n]` is equal to '#', then 'NO' is printed.
    #State of the program after the if-else block has been executed: *`n` is an integer such that 2 ≤ `n` ≤ 100; `k` is an integer such that 1 ≤ `k` ≤ `n` - 1; if either `g == -1` or `t == -1`, the state remains unchanged regarding `n`, `k`, `g`, and `t`. Otherwise, if both `g` and `t` are not -1, "YES" is printed if the absolute difference between `t` and `g` is divisible by `k` and for every `i` in the range from 0 to (abs(t - g) // k), `s[(g + i * k) % n]` is not '#'. If either condition is not met, "NO" is printed.
#Overall this is what the function does:The function accepts two integers `n` and `k`, followed by a string `s` of length `n` that contains exactly one 'G', one 'T', and any combination of '.' and '#'. It checks if it is possible to reach 'T' from 'G' by moving `k` steps at a time, without encountering any obstacles represented by '#'. If 'G' or 'T' are not found in the string, it prints 'NO'. If the absolute difference between the indices of 'G' and 'T' is divisible by `k` and there are no obstacles in the path, it prints 'YES'; otherwise, it prints 'NO'.

