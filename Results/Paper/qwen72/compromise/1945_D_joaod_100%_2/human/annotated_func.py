#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n and m are integers where 1 ≤ m ≤ n ≤ 200,000, a is a list of n integers where 1 ≤ a_i ≤ 10^9, and b is a list of n integers where 1 ≤ b_i ≤ 10^9.
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
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `n` and `m` are integers where 1 ≤ m ≤ n ≤ 200,000, `a` is a list of n integers where 1 ≤ a_i ≤ 10^9, `b` is a list of n integers where 1 ≤ b_i ≤ 10^9, `cases` is the number of iterations the loop has run, `c` is `cases - 1`, `na_frente` is the last input integer minus 1, `pos_final` is the last input integer minus `cases`, `custo_pra_trocar_a` and `custo_pra_passar_b` are lists of integers provided by the user, `v` is -1, `total` is the sum of the minimum of `custo_pra_trocar_a[i]` and `custo_pra_passar_b[i]` for all `i` from `na_frente` to 0, and `best` is the minimum value of `total + custo_pra_trocar_a[i]` for all `i` from `na_frente` to 0 where `i` ≤ `pos_final`.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads two integers `na_frente` and `pos_final`, followed by two lists of integers `custo_pra_trocar_a` and `custo_pra_passar_b`. It calculates the minimum cost to move from `na_frente` to `pos_final` using the costs provided in the lists. The function prints the minimum cost for each test case. After processing all test cases, the function ends, and the state includes the number of test cases processed, the last values of `na_frente` and `pos_final`, and the lists `custo_pra_trocar_a` and `custo_pra_passar_b` provided by the user.

