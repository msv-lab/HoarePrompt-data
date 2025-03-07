#State of the program right berfore the function call: The function `func` is expected to take input parameters, but they are not defined in the provided function signature. Based on the problem description, the function should take the following parameters: `t` (an integer representing the number of test cases), `n`, `k`, `P_B`, `P_S` (integers for each test case representing the length of the permutation, the duration of the game, and the starting positions of Bodya and Sasha, respectively), `p` (a list of integers representing the permutation), and `a` (a list of integers representing the array). The parameters should satisfy the constraints: 1 ≤ t ≤ 10^4, 1 ≤ P_B, P_S ≤ n ≤ 2·10^5, 1 ≤ k ≤ 10^9, 1 ≤ p_i ≤ n, and 1 ≤ a_i ≤ 10^9. The sum of values of n over all test cases does not exceed 2·10^5.
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
        
    #State: The loop will execute `t` times, and for each test case, it will print either 'Bodya', 'Sasha', or 'Draw' based on the comparison of `bm` and `sm` after the inner loop completes. The values of `n`, `k`, `b`, `s`, `p`, `a`, `bm`, `sm`, `bp`, and `sp` will be modified within each test case but will be reset for the next test case. After all iterations, the final values of these variables will be the state after the last test case.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by the parameters `n`, `k`, `P_B`, `P_S`, `p`, and `a`. For each test case, it calculates the scores for two players, Bodya and Sasha, based on their movements and the values in the array `a`. The function then prints the outcome of the game for each test case, which can be 'Bodya', 'Sasha', or 'Draw', depending on the comparison of their final scores. After processing all test cases, the function concludes, and the final state of the program is the state after the last test case, with the results printed for each test case.

