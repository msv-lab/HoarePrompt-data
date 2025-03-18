#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; for each test case, n and m are integers where 1 ≤ m ≤ n ≤ 200,000; a is a list of n integers where 1 ≤ a_i ≤ 10^9; b is a list of n integers where 1 ≤ b_i ≤ 10^9. The sum of n over all test cases does not exceed 2 * 10^5.
def func():
    cases = int(input())
    for c in range(cases):
        na_frente, pos_final = map(int, input().split())
        
        custo_pra_trocar_a = list(map(int, input().split()))
        
        custo_pra_passar_b = list(map(int, input().split()))
        
        na_frente -= 1
        
        pos_final -= 1
        
        total = 0
        
        best = 10 ** 12
        
        for v in range(na_frente, -1, -1):
            if v <= pos_final:
                if best > total + custo_pra_trocar_a[v]:
                    best = total + custo_pra_trocar_a[v]
                if custo_pra_trocar_a[v] < custo_pra_passar_b[v]:
                    total += custo_pra_trocar_a[v]
                else:
                    total += custo_pra_passar_b[v]
            elif custo_pra_trocar_a[v] < custo_pra_passar_b[v]:
                total += custo_pra_trocar_a[v]
            else:
                total += custo_pra_passar_b[v]
        
        print(best)
        
    #State: After the loop executes all its iterations, `c` will be equal to `cases`, indicating that all test cases have been processed. For each test case, `na_frente` and `pos_final` will be adjusted to their respective indices (decremented by 1), and the variable `total` will hold the cumulative sum of the minimum costs between `custo_pra_trocar_a[v]` and `custo_pra_passar_b[v]` for each `v` from `na_frente` down to 0. The variable `best` will hold the minimum value between the initial `best` (10^12) and the sum of `total` plus `custo_pra_trocar_a[v]` for any `v` where `v <= pos_final`. The variable `v` will be -1, indicating the loop has completed its iterations. The variables `t`, `n`, `m`, `a`, `b`, `cases`, `custo_pra_trocar_a`, and `custo_pra_passar_b` remain unchanged.
#Overall this is what the function does:The function reads multiple test cases from the standard input. For each test case, it reads two integers `na_frente` and `pos_final`, followed by two lists of integers `custo_pra_trocar_a` and `custo_pra_passar_b`. It calculates the minimum cost to move from position `na_frente` to `pos_final` using the costs provided in the lists. The function prints the minimum cost for each test case. After processing all test cases, the function completes without returning any value. The state of the program remains unchanged except for the printed output.

