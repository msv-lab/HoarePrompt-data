#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each of the t test cases, n, k, P_B, P_S are integers where 1 ≤ P_B, P_S ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. p is a permutation of length n with elements 1 ≤ p_i ≤ n. a is an array of length n with elements 1 ≤ a_i ≤ 10^9. The sum of values of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The values of `t`, `n`, `k`, `P_B`, `P_S`, `p`, and `a` remain unchanged. The loop iterates `t` times, and for each iteration, it modifies the values of `b`, `s`, `sp`, `bp`, `bm`, and `sm`. After the loop completes, `b` and `s` will be indices that have been updated based on the permutation `p`, and `sp`, `bp`, `bm`, and `sm` will have been updated based on the calculations within the loop. The final output for each iteration will be either 'Bodya', 'Sasha', or 'Draw' depending on the comparison between `bm` and `sm`.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads integers `n`, `k`, `P_B`, and `P_S`, followed by a permutation `p` of length `n` and an array `a` of length `n`. It then performs a series of calculations to determine and print the result of a comparison between two computed values, `bm` and `sm`. The final output for each test case will be either 'Bodya', 'Sasha', or 'Draw' based on whether `bm` is greater than, less than, or equal to `sm`, respectively. The function does not modify the input parameters `t`, `n`, `k`, `P_B`, `P_S`, `p`, or `a` across different test cases.

