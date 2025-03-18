#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, k, P_B, P_S are integers such that 1 ≤ P_B, P_S ≤ n ≤ 2 × 10^5 and 1 ≤ k ≤ 10^9, representing the length of the permutation, the duration of the game, and the starting positions of Bodya and Sasha, respectively. p is a permutation of length n, where each p_i is an integer such that 1 ≤ p_i ≤ n. a is an array of length n, where each a_i is an integer such that 1 ≤ a_i ≤ 10^9. The sum of values of n over all test cases does not exceed 2 × 10^5.
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
        
    #State: The loop iterates through each test case, updating the positions and scores of Bodya and Sasha based on the permutation `p` and the array `a`. After each test case, the loop prints 'Bodya' if Bodya's score is greater than Sasha's score, 'Sasha' if Sasha's score is greater than Bodya's score, and 'Draw' if both scores are equal. The variables `t`, `n`, `k`, `P_B`, `P_S`, `p`, and `a` are reset for each test case, and the final state of these variables is not defined as they are re-initialized for each test case. The loop completes all iterations, and the output state is the result of the comparisons for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by the parameters `n`, `k`, `P_B`, `P_S`, `p`, and `a`. For each test case, it simulates a game where two players, Bodya and Sasha, move through a permutation `p` and collect scores based on the values in array `a`. The function updates the positions and scores of the players over `k` turns and then determines the winner by comparing their final scores. The function prints 'Bodya' if Bodya's score is higher, 'Sasha' if Sasha's score is higher, and 'Draw' if both scores are equal. After processing all test cases, the function completes and the final state is the set of printed results for each test case.

