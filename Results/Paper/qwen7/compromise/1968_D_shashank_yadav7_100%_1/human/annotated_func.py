#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each testcase, n, k, P_B, P_S are integers such that 1 ≤ P_B, P_S ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9; p is a list of n integers representing the permutation p where 1 ≤ p_i ≤ n; a is a list of n integers where 1 ≤ a_i ≤ 10^9.
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
            bm = max(bm, a[b] * k + bp)
            sm = max(sm, a[s] * k + sp)
            sp += a[s]
            bp += a[b]
        
        if bm > sm:
            print('Bodya')
        elif bm < sm:
            print('Sasha')
        else:
            print('Draw')
        
    #State: After the loop executes all iterations, `i` will be `n + t - 1`, `k` will be 0, `b` will be `p[b] - 2^t`, `s` will be `p[s] - 2^t`, `bm` will be the maximum value between `bm` and `a[b] * k + bp` after `n * t` iterations, `sm` will be the maximum value between `sm` and `a[s] * k + sp` after `n * t` iterations, `sp` will be the sum of `a[s]` added `n * t` times to `sp`, `bp` will be the sum of `a[b]` added `n * t` times to `bp`, and either `bm` will be greater than `sm` or `bm` will be greater than or equal to `sm` after the if-else block executes.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers t, n, k, P_B, P_S, and lists p and a. For each test case, it updates indices b and s based on permutations and iterates through the list a, calculating maximum values bm and sm under certain conditions. Finally, it prints 'Bodya', 'Sasha', or 'Draw' based on the comparison between bm and sm.

