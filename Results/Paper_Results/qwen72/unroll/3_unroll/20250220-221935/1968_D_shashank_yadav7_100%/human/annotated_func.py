#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each of the t test cases, n, k, P_B, P_S are integers where 1 ≤ P_B, P_S ≤ n ≤ 2·10^5 and 1 ≤ k ≤ 10^9. p is a permutation of length n, and a is an array of length n where each element a_i is an integer such that 1 ≤ a_i ≤ 10^9. The sum of values of n over all test cases does not exceed 2·10^5.
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
        
    #State: The loop iterates through `t` test cases, and for each test case, it processes the integers `n`, `k`, `P_B`, `P_S`, the permutation `p`, and the array `a`. After the loop, the values of `t`, `n`, `k`, `P_B`, `P_S`, `p`, and `a` remain unchanged. The variables `b` and `s` are modified within the loop but are reset for each new test case. The variables `sp`, `bp`, `bm`, and `sm` are used to calculate the scores for each test case and are reset for each new test case. The output state for each test case is either 'Bodya', 'Sasha', or 'Draw' based on the comparison of `bm` and `sm`.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads the integers `n`, `k`, `P_B`, and `P_S`, a permutation `p` of length `n`, and an array `a` of length `n`. It then calculates two scores, `bm` and `sm`, based on the elements of `a` and the permutation `p`. After the calculations, it prints 'Bodya' if `bm` is greater than `sm`, 'Sasha' if `bm` is less than `sm`, or 'Draw' if they are equal. The function does not return any values; it only prints the results of the comparisons for each test case.

