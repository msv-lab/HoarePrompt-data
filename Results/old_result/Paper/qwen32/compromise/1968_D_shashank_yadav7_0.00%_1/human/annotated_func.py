#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each of the t test cases, n, k, P_B, and P_S are positive integers such that 1 <= P_B, P_S <= n <= 2 * 10^5 and 1 <= k <= 10^9. The permutation p is a list of n integers where each integer is between 1 and n inclusive, and the array a is a list of n integers where each integer is between 1 and 10^9 inclusive. The sum of all n values across all test cases does not exceed 2 * 10^5.
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
        
    #State: After all iterations, `t` remains unchanged, `n`, `k`, `b`, `s`, `p`, `a`, `sp`, `bp`, `bm`, and `sm` are updated based on the input for each iteration, and the result of each comparison between `bm` and `sm` is printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `k`, `P_B`, and `P_S`, and two lists `p` and `a`. For each test case, it calculates scores for two entities, Bodya and Sasha, based on the given rules and prints the name of the entity with the higher score, or "Draw" if the scores are equal.

