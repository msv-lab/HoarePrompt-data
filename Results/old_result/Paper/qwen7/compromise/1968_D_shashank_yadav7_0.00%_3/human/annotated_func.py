#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each testcase, n, k, P_B, P_S are positive integers such that 1 ≤ P_B, P_S ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9; p is a permutation of length n; a is an array of positive integers such that 1 ≤ a_i ≤ 10^9 for all i.
def func():
    t = int(input())
    for i in range(t):
        n, k, b, s = list(map(int, input().split()))
        
        p = list(map(int, input().split()))
        
        a = list(map(int, input().split()))
        
        b -= 1
        
        s -= 1
        
        sp = a[s]
        
        bp = a[b]
        
        bm = a[b] * k
        
        sm = a[s] * k
        
        for i in range(n):
            k -= 1
            if k == 0:
                break
            b = p[b] - 1
            s = p[s] - 1
            bm += max(bm, a[b] * k + bp)
            sm += max(sm, a[s] * k + sp)
            sp += a[s]
            bp += a[b]
        
        if bm > sm:
            print('Bodya')
        elif bm < sm:
            print('Sasha')
        else:
            print('Draw')
        
    #State: After all iterations of the loop have finished, the variable `i` will be equal to `-t`, `k` will be `0`, `b` will be `p[p[...]] - t` (where `p` is applied `t-1` times to `b`), `s` will be `p[p[...]] - t` (where `p` is applied `t-1` times to `s` and then subtracted by `t-1`), `bm` will be the cumulative maximum of `a[b] * k + bp` over all `t` iterations, `sm` will be the cumulative maximum of `a[s] * k + sp` over all `t` iterations, `sp` will be the sum of `a[s]` over all `t` iterations, and `bp` will be the sum of `a[b]` over all `t` iterations.
#Overall this is what the function does:The function processes multiple test cases, each defined by values of \( t \), \( n \), \( k \), \( b \), \( s \), a permutation \( p \), and an array \( a \). For each test case, it calculates two cumulative maximum values, \( bm \) and \( sm \), based on the values in \( a \) and the indices \( b \) and \( s \) modified by the permutation \( p \) and the count \( k \). Finally, it prints 'Bodya' if \( bm \) is greater than \( sm \), 'Sasha' if \( sm \) is greater than \( bm \), and 'Draw' if they are equal.

