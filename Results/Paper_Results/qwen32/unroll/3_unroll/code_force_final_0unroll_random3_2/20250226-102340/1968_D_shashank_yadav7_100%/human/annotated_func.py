#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each of the t test cases, n, k, P_B, and P_S are integers such that 1 <= P_B, P_S <= n <= 2 * 10^5 and 1 <= k <= 10^9. p is a list of n integers where each element p_i satisfies 1 <= p_i <= n. a is a list of n integers where each element a_i satisfies 1 <= a_i <= 10^9. The sum of all n values across all test cases does not exceed 2 * 10^5.
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
        
    #State: the series of 'Bodya', 'Sasha', or 'Draw' for each test case.
#Overall this is what the function does:The function processes multiple test cases, each involving a series of positions and values. For each test case, it determines whether 'Bodya' or 'Sasha' has a higher score based on the given rules, or if it's a 'Draw'. The score is calculated by traversing a list of positions and accumulating values, with a limit on the number of steps (`k`). The function outputs 'Bodya', 'Sasha', or 'Draw' for each test case.

