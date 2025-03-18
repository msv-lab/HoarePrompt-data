#State of the program right berfore the function call: The function `func` is expected to take input through standard input or a predefined method, not as parameters. The input consists of multiple test cases. For each test case, the first line contains four integers n, k, P_B, P_S where 1 ≤ P_B, P_S ≤ n ≤ 2·10^5 and 1 ≤ k ≤ 10^9. The second line contains n integers p_1, ..., p_n representing the permutation, where 1 ≤ p_i ≤ n. The third line contains n integers a_1, ..., a_n representing the array, where 1 ≤ a_i ≤ 10^9. The sum of values of n over all test cases does not exceed 2·10^5.
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
        
    #State: `t` is greater than 0, `i` is `t - 1`, `n` is the input integer, `k` is 0 or the initial value of `k` minus the number of iterations that were executed, `b` is the final value of `p[p[...p[b] - 1... - 1] - 1]` (where the number of nested `p[b] - 1` operations is equal to the number of iterations executed), `s` is the final value of `p[p[...p[s] - 1... - 1] - 1]` (where the number of nested `p[s] - 1` operations is equal to the number of iterations executed), `sp` is the sum of the initial value of `sp` and the values at the indices `s` in `a` for each iteration, `bp` is the sum of the initial value of `bp` and the values at the indices `b` in `a` for each iteration, `bm` is the maximum value of `a[b] * k + bp` for each iteration, `sm` is the maximum value of `a[s] * k + sp` for each iteration. If `bm` is greater than `sm`, the condition `bm > sm` holds. If `bm` is less than `sm`, the condition `bm < sm` holds. If `bm` is equal to `sm`, the condition `bm == sm` holds.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input. Each test case consists of four integers `n`, `k`, `P_B`, and `P_S`, followed by a permutation of `n` integers and an array of `n` integers. It processes these inputs to determine the winner of a game between two players, Bodya and Sasha, or if the game ends in a draw. The final state of the program after the function concludes is that for each test case, it prints either 'Bodya', 'Sasha', or 'Draw' to the standard output. The variables `t`, `i`, `n`, `k`, `b`, `s`, `sp`, `bp`, `bm`, and `sm` are modified during the execution, but their final values are not returned or used outside the function.

