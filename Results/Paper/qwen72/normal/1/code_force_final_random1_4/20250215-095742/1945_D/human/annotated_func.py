#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; for each test case, n and m are integers where 1 ≤ m ≤ n ≤ 200,000; a_i and b_i are lists of integers of length n where 1 ≤ a_i, b_i ≤ 10^9.
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
        
    #State: After all iterations of the loop, `t`, `n`, `m`, `a_i`, `b_i`, and `cases` retain their initial values. The variable `c` will be equal to `cases`, indicating that the loop has run the number of times specified by `cases`. The variables `na_frente` and `pos_final` will be one less than their initial values for each iteration, but since they are reset for each new test case, their final values depend on the last test case's inputs. The lists `custo_pra_trocar_a` and `custo_pra_passar_b` will retain the values provided by the user for each test case. The variable `total` will be the sum of the minimum costs (`custo_pra_trocar_a[v]` or `custo_pra_passar_b[v]`) for each `v` from `na_frente` down to 0, considering the conditions within the loop. The variable `best` will be the minimum value between its initial value (10^12) and the sum of `total` plus `custo_pra_trocar_a[v]` for any `v` that satisfies `v <= pos_final`.
#Overall this is what the function does:The function processes a series of test cases, each defined by two integers `n` and `m`, and two lists of integers `a_i` and `b_i`. For each test case, it calculates the minimum cost required to move from a starting position to a final position, considering two types of costs: the cost to change positions (`a_i`) and the cost to pass through positions (`b_i`). The function prints the minimum cost for each test case. After processing all test cases, the function retains the initial values of the input parameters and any variables used within the loop are reset for each new test case. The final state of the program includes the printed results for each test case and the input variables remain unchanged.

