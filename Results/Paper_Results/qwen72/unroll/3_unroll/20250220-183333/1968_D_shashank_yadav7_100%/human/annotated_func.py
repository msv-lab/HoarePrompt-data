#State of the program right berfore the function call: The function `func` is intended to solve a game problem but lacks parameters in its definition. The correct function definition should include parameters for the number of test cases `t`, the length of the permutation `n`, the duration of the game `k`, the starting positions of Bodya and Sasha `P_B` and `P_S`, the permutation `p`, and the array `a`. The parameters should satisfy: 1 ≤ t ≤ 10^4, 1 ≤ P_B, P_S ≤ n ≤ 2·10^5, 1 ≤ k ≤ 10^9, 1 ≤ p_i ≤ n, 1 ≤ a_i ≤ 10^9, and the sum of values of n over all test cases does not exceed 2·10^5.
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
        
    #State: The loop iterates `t` times, processing each test case. For each test case, the variables `n`, `k`, `b`, `s`, `p`, and `a` are updated based on the input. After processing each test case, the loop prints 'Bodya', 'Sasha', or 'Draw' based on the comparison of `bm` and `sm`. The values of `t`, `n`, `k`, `b`, `s`, `p`, and `a` are reset for the next test case, and the loop continues until all `t` test cases are processed.
#Overall this is what the function does:The function `func` processes a series of game scenarios. For each scenario, it reads the number of test cases `t`, the length of the permutation `n`, the duration of the game `k`, the starting positions of Bodya and Sasha `P_B` and `P_S`, the permutation `p`, and the array `a`. It then iterates through each test case, updating the positions and scores of Bodya and Sasha based on the permutation and the array. After processing each test case, it prints the result indicating whether Bodya, Sasha, or neither (a draw) has a higher score. The function does not return any values; it only prints the results.

