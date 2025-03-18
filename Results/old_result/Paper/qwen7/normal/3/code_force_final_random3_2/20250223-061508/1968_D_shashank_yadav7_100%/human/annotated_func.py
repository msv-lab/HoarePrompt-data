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
        
    #State: Output State: All the variables `n`, `k`, `b`, `s`, `sp`, `bp`, and `bm` will retain their final values from the last iteration of the loop. Specifically, `n` will be 0, `k` will be 0, `b` will be the result of `p[b] - 1` after the last iteration, `s` will be the result of `p[s] - 1` after the last iteration, `sp` will be the cumulative sum of `a[s]` after the last iteration, `bp` will be the cumulative sum of `a[b]` after the last iteration, and `bm` will be the maximum value it attained during any iteration of the loop.
    #
    #This means that after all iterations, `bm` will be the highest value it reached when comparing `a[b] * k + bp` and `a[s] * k + sp` across all iterations, while `sp` and `bp` will reflect the sums accumulated from the respective indices `s` and `b`. The values of `n` and `k` will be 0, indicating that the loop has completed its iterations.
#Overall this is what the function does:The function processes a series of test cases, each consisting of integers \( n \), \( k \), \( P_B \), \( P_S \), a permutation \( p \) of length \( n \), and an array \( a \) of positive integers. For each test case, it calculates two values, \( bm \) and \( sm \), which represent the maximum possible sums obtained by applying a specific operation involving elements of \( a \) and \( k \). After processing all test cases, it prints 'Bodya' if \( bm \) is greater than \( sm \), 'Sasha' if \( bm \) is less than \( sm \), and 'Draw' if they are equal.

