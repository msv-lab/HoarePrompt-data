#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n and m are integers where 1 ≤ m ≤ n ≤ 200,000, a_i and b_i are lists of integers of length n where 1 ≤ a_i, b_i ≤ 10^9.
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
        
    #State: The loop iterates through each case, and for each case, it calculates the minimum cost to move an element from a position `na_frente` to a position `pos_final` using the costs provided in `custo_pra_trocar_a` and `custo_pra_passar_b`. After all iterations, the variable `best` holds the minimum cost for the current case, and this value is printed. The variables `na_frente`, `pos_final`, `custo_pra_trocar_a`, `custo_pra_passar_b`, and `total` are reset for each new case. The loop variable `c` will have incremented by 1 for each iteration, and after the loop finishes, `c` will be equal to `cases`.
#Overall this is what the function does:The function `func` processes a series of cases, where each case involves calculating the minimum cost to move an element from a specified starting position (`na_frente`) to a specified ending position (`pos_final`) using two lists of costs (`custo_pra_trocar_a` and `custo_pra_passar_b`). For each case, the function reads the input values, computes the minimum cost, and prints this cost. The function does not return any value; it only prints the results. After processing all cases, the function concludes, and the state of the program is such that all input values have been processed and the minimum costs for each case have been printed.

