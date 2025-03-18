#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each testcase consists of four integers n, k, P_B, P_S where 1 <= P_B, P_S <= n <= 2 * 10^5 and 1 <= k <= 10^9. The next line contains n integers p_1, ..., p_n (1 <= p_i <= n) representing the permutation p. The following line contains n integers a_1, ..., a_n (1 <= a_i <= 10^9) representing the array a. The sum of all n across all testcases does not exceed 2 * 10^5.
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
        
    #State: t is an input integer such that 1 <= t <= 10^4, n is the number of elements in the permutation and array for the last test case, k is either 0 or the initial k minus the number of iterations, b is the final value of b after all iterations for the last test case, s is the final value of s after all iterations for the last test case, p is the permutation list for the last test case, a is the array list for the last test case, i is the number of iterations the inner loop ran for the last test case, sp is the cumulative sum of a[s] for the last test case, bp is the cumulative sum of a[b] for the last test case, bm is the maximum value of a[b] * k + bp for the last test case, sm is the maximum value of a[s] * k + sp for the last test case.
#Overall this is what the function does:The function reads multiple test cases, each consisting of integers `n`, `k`, `P_B`, and `P_S`, a permutation `p` of length `n`, and an array `a` of length `n`. For each test case, it calculates and compares the maximum possible values of two expressions involving elements from `a` and the permutation `p`, adjusted by `k`. It then prints "Bodya" if one expression is greater, "Sasha" if the other is greater, or "Draw" if they are equal.

