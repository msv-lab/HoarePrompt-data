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
        
    #State: The loop has processed `cases` number of test cases. For each test case, it has read `na_frente` and `pos_final` as integers, and two lists of integers `custo_pra_trocar_a` and `custo_pra_passar_b` of length `n`. It has then calculated the minimum cost to move from the position `na_frente` to `pos_final` using the provided costs, and printed this minimum cost. The variables `na_frente`, `pos_final`, `custo_pra_trocar_a`, `custo_pra_passar_b`, `total`, and `best` are reset for each iteration of the loop. After all iterations, the loop has completed and the program has printed the minimum cost for each test case.
#Overall this is what the function does:The function reads a number of test cases `t` and for each test case, it reads two integers `na_frente` and `pos_final`, followed by two lists of integers `custo_pra_trocar_a` and `custo_pra_passar_b` of length `n`. It calculates the minimum cost to move from the position `na_frente` to `pos_final` using the provided costs, and prints this minimum cost for each test case. The function does not return any value; it only prints the results. After processing all test cases, the function completes and the program ends.

