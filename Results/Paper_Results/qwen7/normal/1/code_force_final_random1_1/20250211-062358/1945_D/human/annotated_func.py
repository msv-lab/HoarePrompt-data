#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers satisfying 1 ≤ m ≤ n ≤ 200,000. a and b are lists of n positive integers where 1 ≤ a_i, b_i ≤ 10^9 for all 1 ≤ i ≤ n.
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
        
    #State: After all iterations of the loop, `v` will be -1, `best` will hold the minimum value found during all iterations of the loop, `na_frente` will be less than or equal to -1, and `total` will be the cumulative cost based on the conditions specified in the loop body.
#Overall this is what the function does:The function processes multiple test cases, each defined by two positive integers \(n\) and \(m\), and two lists of \(n\) positive integers \(a\) and \(b\). For each test case, it calculates the minimum cost to move from position \(na_frente\) to position \(pos_final\) using either the cost from list \(a\) or list \(b\), depending on which is cheaper at each step. The function then prints the minimum cost found for each test case.

