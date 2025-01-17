#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4; for each test case, n and m are positive integers such that 1 <= n <= 2 * 10^5 and 0 <= m <= 2 * 10^6; the list a contains n integers such that 1 <= a_i <= 10^9 for all elements a_i in the list.
def func():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        a = list(map(str, input().split()))
        
        len_arr = [0] * n
        
        zrr = [0] * n
        
        ans = 0
        
        for i in range(n):
            len_arr[i] = len(a[i])
            zrr[i] = len(a[i]) - len(a[i].rstrip('0'))
            ans += len_arr[i] - zrr[i]
        
        zrr.sort(reverse=True)
        
        for i in range(n):
            if i % 2 != 0:
                ans += zrr[i]
        
        if ans - 1 >= m:
            print('Sasha')
        else:
            print('Anna')
        
    #State of the program after the  for loop has been executed: `t` is an integer (1), `n` is the largest integer `n` provided in any of the inputs, `m` is the largest integer `m` provided in any of the inputs, `a` is a list of strings with the maximum length of `n`, `len_arr` is a list of integers containing the lengths of the strings in `a`, `zrr` is a list of integers sorted in descending order containing the differences between the lengths of the strings and the lengths of the strings after stripping trailing zeros, and `ans` is the sum of `len_arr[i] - zrr[i]` for all `i` in the range `[0, n-1]`, plus the sum of `zrr[i]` where `i` is odd. If `ans - 1 >= m`, the function prints 'Sasha'. Otherwise, it prints 'Anna'.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it reads two integers `n` and `m`, and a list `a` of `n` space-separated strings, where each string consists of digits. It calculates the sum of the lengths of these strings after removing trailing zeros (`ans`). Then, it sorts the differences between the original lengths and the lengths after removing trailing zeros in descending order (`zrr`). Finally, it adds the values in `zrr` corresponding to odd indices to `ans`. Based on whether `ans - 1` is greater than or equal to `m`, the function prints either 'Sasha' or 'Anna'. The function handles the following edge cases:
1. The input list `a` can contain empty strings, which are treated as having zero length after removing trailing zeros.
2. The input `m` can be zero, and the function still calculates and compares `ans - 1` with `m`.
3. The function correctly processes multiple test cases sequentially, ensuring that each test case is independent of the others.

