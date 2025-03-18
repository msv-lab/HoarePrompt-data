#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n and m are integers where 1 ≤ m ≤ n ≤ 200,000, a is a list of n integers where 1 ≤ a_i ≤ 10^9, b is a list of n integers where 1 ≤ b_i ≤ 10^9, and the sum of n over all test cases does not exceed 2 × 10^5.
def func():
    cases = int(input())
    for c in range(cases):
        na_frente, pos_final = map(int, input().split())
        
        custo_pra_trocar_a = list(map(int, input().split()))
        
        custo_pra_passar_b = list(map(int, input().split()))
        
        na_frente -= 1
        
        pos_final -= 1
        
        total = 0
        
        best = sys.float_info.max
        
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
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `n` and `m` are integers where 1 ≤ m ≤ n ≤ 200,000, `a` is a list of n integers where 1 ≤ a_i ≤ 10^9, `b` is a list of n integers where 1 ≤ b_i ≤ 10^9, the sum of n over all test cases does not exceed 2 × 10^5, `cases` is an input integer that must be greater than 0, `c` is `cases - 1`, `na_frente` is -1, `pos_final` is the last input integer minus 1, `custo_pra_trocar_a` and `custo_pra_passar_b` are lists of integers read from input, `total` is the sum of the minimum values between `custo_pra_trocar_a[v]` and `custo_pra_passar_b[v]` for all `v` from `na_frente` (initial value) to 0, and `best` is the minimum value of `total + custo_pra_trocar_a[v]` for all `v` from `na_frente` (initial value) to 0 that are less than or equal to `pos_final`.
#Overall this is what the function does:The function `func` reads multiple test cases from input. For each test case, it reads two integers `na_frente` and `pos_final`, followed by two lists of integers `custo_pra_trocar_a` and `custo_pra_passar_b`. It calculates the minimum cost to move from position `na_frente` to `pos_final` by either swapping elements or passing through them, and prints the best (minimum) cost found. The function does not return any value; it only prints the results. After the function concludes, the state of the program includes the input variables `t`, `n`, `m`, `a`, and `b` remaining unchanged, and the calculated best cost for each test case being printed.

