#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, k, P_B, P_S are integers where 1 ≤ P_B, P_S ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9, representing the length of the permutation, the duration of the game, and the starting positions of Bodya and Sasha, respectively. p is a permutation of length n, containing integers from 1 to n. a is an array of length n, containing integers where 1 ≤ a_i ≤ 10^9. The sum of values of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `i` is `t-1`, `n` is the initial value of `n`, `t` is the initial value of `t`, `k` is the initial value of `k` minus the number of iterations (or -1 if the loop breaks early), `b` is the final position of `b` after all iterations (or the position when `k` reaches 0), `s` is the final position of `s` after all iterations (or the position when `k` reaches 0), `bm` is the maximum value of `a[b] * k + bp` over all iterations, `sm` is the maximum value of `a[s] * k + sp` over all iterations, `sp` is the sum of `a[s]` for each `s` during the loop, `bp` is the sum of `a[b]` for each `b` during the loop. If `k` reaches 0 at any point, the loop breaks and `bm` and `sm` are set to -1. If `bm` is greater than `sm`, `bm` is greater than `sm`. Otherwise, `bm` is less than or equal to `sm`.
#Overall this is what the function does:The function `func` reads multiple test cases, each defined by parameters `n`, `k`, `P_B`, `P_S`, `p`, and `a`. For each test case, it calculates the maximum possible scores for two players, Bodya and Sasha, based on their movements and the values in the permutation `p` and array `a`. The function then prints the result of the game for each test case: 'Bodya' if Bodya's maximum score is greater, 'Sasha' if Sasha's maximum score is greater, and 'Draw' if their scores are equal. After processing all test cases, the function concludes.

