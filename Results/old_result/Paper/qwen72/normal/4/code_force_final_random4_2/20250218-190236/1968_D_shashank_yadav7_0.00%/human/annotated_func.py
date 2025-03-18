#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, k, P_B, P_S are integers where 1 ≤ P_B, P_S ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9, representing the length of the permutation, the duration of the game, and the starting positions of Bodya and Sasha, respectively. p is a list of n integers where 1 ≤ p_i ≤ n, representing the elements of the permutation p. a is a list of n integers where 1 ≤ a_i ≤ 10^9, representing the elements of the array a.
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
        
    #State: The loop has completed all `t` iterations. `i` is `t - 1`. `n`, `k`, `b`, and `s` are the final values after the last iteration. `p` and `a` remain unchanged. `sp` is the sum of the integers at the indices `p[s] - 1` after each iteration, plus the initial `a[s]`. `bp` is the sum of the integers at the indices `p[b] - 1` after each iteration, plus the initial `a[b]`. `bm` is the sum of the maximum values between the initial `bm` and `a[b] * (k - i) + bp` for each iteration. `sm` is the sum of the maximum values between the initial `sm` and `a[s] * (k - i) + sp` for each iteration. If `k` reaches 0 before the loop completes, the loop breaks and the final state is determined at that point. If `bm` is greater than `sm`, then `bm` is greater than `sm`. Otherwise, `bm` is less than or equal to `sm`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads integers `n`, `k`, `P_B`, and `P_S` representing the length of a permutation, the duration of a game, and the starting positions of two players, Bodya and Sasha, respectively. It also reads a permutation `p` of length `n` and an array `a` of length `n`. The function then simulates a game where Bodya and Sasha move according to the permutation `p` and the array `a` for `k` steps. After the simulation, it compares the scores of Bodya and Sasha and prints 'Bodya' if Bodya's score is higher, 'Sasha' if Sasha's score is higher, or 'Draw' if their scores are equal. The function does not return any value but prints the result for each test case. After processing all test cases, the function concludes, and the input variables `t`, `n`, `k`, `P_B`, `P_S`, `p`, and `a` remain unchanged.

