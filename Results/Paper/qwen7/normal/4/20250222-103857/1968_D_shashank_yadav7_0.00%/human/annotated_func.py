#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each testcase, n, k, P_B, P_S are integers such that 1 ≤ P_B, P_S ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9. p is a list of n integers representing the permutation, where 1 ≤ p_i ≤ n. a is a list of n integers representing the array, where 1 ≤ a_i ≤ 10^9.
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
        
    #State: All `i` values will be equal to 10000, `k` will be -10000, `b` will be `p[b] - 9999`, `s` will be `p[s] - 9999`, `bm` will be `2^9999 * bm + max(2^9999 * bm, a[b] * -10000 + bp)`, `sm` will be `sm + max(sm, a[s] * -10000 + sp)`, `sp` will be `sum(a[s]) * 9999 + sp`, `bp` will be `sum(a[b]) * 9999 + bp`.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \(t\), \(n\), \(k\), \(P_B\), and \(P_S\), along with lists \(p\) and \(a\). For each test case, it calculates two scores, \(bm\) and \(sm\), by iterating through the permutation \(p\) and updating the scores based on the values in list \(a\) and the remaining count \(k\). After processing all test cases, it prints 'Bodya' if \(bm\) is greater than \(sm\), 'Sasha' if \(bm\) is less than \(sm\), and 'Draw' if they are equal.

