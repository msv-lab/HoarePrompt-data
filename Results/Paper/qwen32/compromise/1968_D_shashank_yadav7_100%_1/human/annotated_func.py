#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each testcase, n, k, P_B, and P_S are integers such that 1 <= P_B, P_S <= n <= 2 * 10^5 and 1 <= k <= 10^9. p is a list of n integers where each integer is between 1 and n inclusive. a is a list of n integers where each integer is between 1 and 10^9 inclusive. The sum of all n values across all testcases does not exceed 2 * 10^5.
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
        
    #State: `t` is an integer such that 1 <= `t` <= 10^4; `i` is `min(n, k) - 1`; `n` is unchanged; `k` is 0 if `k` was greater than or equal to `n`, otherwise `k - min(n, k)`; `b` is `p[p[...p[b]...]] - 1` (updated `min(n, k)` times); `s` is `p[p[...p[s]...]] - 1` (updated `min(n, k)` times); `p` is unchanged; `a` is unchanged; `sp` is the cumulative sum of `a[s]` for `min(n, k)` iterations; `bp` is the cumulative sum of `a[b]` for `min(n, k)` iterations; `bm` is the maximum value of `a[b] * k + bp` for `min(n, k)` iterations; `sm` is the maximum value of `a[s] * k + sp` for `min(n, k)` iterations.
#Overall this is what the function does:The function processes multiple test cases, each involving several integers and two lists. For each test case, it calculates and compares two values based on the given inputs and prints whether "Bodya" wins, "Sasha" wins, or if it is a "Draw".

