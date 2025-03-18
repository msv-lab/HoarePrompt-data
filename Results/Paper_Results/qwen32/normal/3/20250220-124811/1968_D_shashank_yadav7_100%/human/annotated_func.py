#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each testcase, n, k, P_B, and P_S are integers such that 1 <= P_B, P_S <= n <= 2 * 10^5 and 1 <= k <= 10^9. p is a list of n integers where each p_i is an integer such that 1 <= p_i <= n. a is a list of n integers where each a_i is an integer such that 1 <= a_i <= 10^9. The sum of all n values across all test cases does not exceed 2 * 10^5.
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
        
    #State: - `t` will be 0 as all iterations are completed.
    #- `n`, `k`, `b`, `s`, `p`, `a` will be those of the last iteration.
    #- `sp` will be the cumulative sum of `a[s]` over the iterations of the last test case.
    #- `bp` will be the cumulative sum of `a[b]` over the iterations of the last test case.
    #- `bm` will be the maximum value of `a[b] * k + bp` encountered during the last test case.
    #- `sm` will be the maximum value of `a[s] * k + sp` encountered during the last test case.
    #
    #The final output will be either "Bodya", "Sasha", or "Draw" based on the comparison of `bm` and `sm` from the last iteration.
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases where each test case consists of integers `n`, `k`, `P_B`, and `P_S`, a list `p` of `n` integers, and a list `a` of `n` integers. For each test case, it calculates the maximum possible values for Bodya and Sasha based on the given rules and prints "Bodya" if Bodya's value is greater, "Sasha" if Sasha's value is greater, or "Draw" if both values are equal.

