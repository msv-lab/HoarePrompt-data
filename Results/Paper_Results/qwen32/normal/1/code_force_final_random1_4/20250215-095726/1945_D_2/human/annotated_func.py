#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ m ≤ n ≤ 200,000. a is a list of n integers where each element a_i satisfies 1 ≤ a_i ≤ 10^9. b is a list of n integers where each element b_i satisfies 1 ≤ b_i ≤ 10^9. The sum of all n across all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` remains the same, `cases` remains the same, `n` and `m` remain the same, `a` and `b` remain the same, `c` is `cases - 1`, `na_frente` and `pos_final` are from the last test case, `custo_pra_trocar_a` and `custo_pra_passar_b` are from the last test case, `total` is the accumulated cost for the last test case, and `best` is the minimum cost for the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `na_frente` and `pos_final`, and two lists of integers `custo_pra_trocar_a` and `custo_pra_passar_b`. For each test case, it calculates and prints the minimum cost to reach a specific position (`pos_final`) from the starting position (`na_frente`) by either swapping elements or passing through them based on the costs provided in the lists.

