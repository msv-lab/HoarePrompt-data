#State of the program right berfore the function call: The function `func` is expected to take input through standard input or a predefined structure, not as direct function parameters. The input consists of multiple test cases. For each test case, the first line contains four integers n, k, P_B, P_S (1 ≤ P_B, P_S ≤ n ≤ 2·10^5, 1 ≤ k ≤ 10^9), the second line contains n integers p_1, ..., p_n (1 ≤ p_i ≤ n), and the third line contains n integers a_1, ..., a_n (1 ≤ a_i ≤ 10^9). The total sum of n across all test cases does not exceed 2·10^5.
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
        
    #State: The loop has completed all iterations for all test cases. `t` is 0, indicating no more test cases to process. `i` is the total number of test cases processed, which is the initial value of `t`. `n`, `k`, `b`, and `s` are the final values after the last test case has been processed, which could be 0 or some other value depending on the input. `p` and `a` are lists that have been processed and are in their final state after the last test case. `sp` and `bp` are the sums of the values from the `a` list at the indices `s` and `b` respectively, accumulated over all iterations of the last test case. `bm` and `sm` are the maximum values of the expressions `a[b] * k + bp` and `a[s] * k + sp` respectively, computed over all iterations of the last test case. If `bm` is greater than `sm`, the program has printed 'Bodya' for the last test case. If `bm` is less than `sm`, the program has printed 'Sasha' for the last test case. If `bm` is equal to `sm`, the program has printed 'Draw' for the last test case.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input. Each test case consists of three lines: the first line contains four integers `n`, `k`, `P_B`, and `P_S` (where 1 ≤ P_B, P_S ≤ n ≤ 2·10^5 and 1 ≤ k ≤ 10^9), the second line contains `n` integers `p_1, ..., p_n` (where 1 ≤ p_i ≤ n), and the third line contains `n` integers `a_1, ..., a_n` (where 1 ≤ a_i ≤ 10^9). The function processes each test case by adjusting the values of `b` and `s` based on the `p` list and calculates the maximum possible values of two expressions involving elements from the `a` list. After processing, it prints 'Bodya' if the first expression is greater, 'Sasha' if the second expression is greater, or 'Draw' if they are equal. The function continues processing until all test cases are completed.

