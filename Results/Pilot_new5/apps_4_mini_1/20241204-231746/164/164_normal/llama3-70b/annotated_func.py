#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 100, k is an integer such that 1 ≤ k ≤ n - 1, and the input string of length n contains exactly one 'G' and one 'T', with the rest being either '.' or '#'.
def func():
    n, k = map(int, input().split())
    s = input()
    g, t = -1, -1
    for i in range(n):
        if s[i] == 'G':
            g = i
        elif s[i] == 'T':
            t = i
        
    #State of the program after the  for loop has been executed: `g` is the index of the last occurrence of 'G' in string `s`, `t` is the index of the last occurrence of 'T' in string `s`, `n` is an integer such that 2 ≤ `n` ≤ 100, `k` is an integer such that 1 ≤ `k` ≤ `n - 1`, and `s` is an input string. If 'G' or 'T' do not appear in `s`, then `g` remains -1 and `t` remains -1.
    if (g == -1 or t == -1) :
        print('NO')
    else :
        if (abs(t - g) % k == 0 and all(s[(g + i * k) % n] != '#' for i in range(abs(t -
    g) // k + 1))) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`g` is the index of the last occurrence of 'G' in string `s`, `t` is the index of the last occurrence of 'T' in string `s`, `n` is an integer such that 2 ≤ `n` ≤ 100, `k` is an integer such that 1 ≤ `k` ≤ `n - 1`, and `s` is an input string. If the absolute difference between `t` and `g` is divisible by `k` and there are no '#' characters in the positions defined by `g + i * k` (modulo `n`) for `i` ranging from 0 to `(abs(t - g) // k)`, the output is 'YES'. Otherwise, the output is 'NO'.
    #State of the program after the if-else block has been executed: *`g` is the index of the last occurrence of 'G' in string `s`, `t` is the index of the last occurrence of 'T' in string `s`, `n` is an integer such that 2 ≤ `n` ≤ 100, and `k` is an integer such that 1 ≤ `k` ≤ `n - 1`. If either 'G' or 'T' do not appear in `s`, the output is 'NO'. Otherwise, if the absolute difference between `t` and `g` is divisible by `k` and there are no '#' characters in the positions defined by `g + i * k` (modulo `n`) for `i` ranging from 0 to `(abs(t - g) // k)`, the output is 'YES'. If these conditions are not met, the output is 'NO'.
#Overall this is what the function does:The function reads two integers `n` and `k`, and a string `s` of length `n` containing exactly one 'G' and one 'T', with the remaining characters either as '.' or '#'. It checks if 'G' can reach 'T' by moving `k` steps at a time without encountering any '#' characters. If 'G' or 'T' is not found, it outputs 'NO'. If the absolute difference between the indices of 'T' and 'G' is divisible by `k` and there are no '#' characters in the way, it outputs 'YES'; otherwise, it outputs 'NO'.

