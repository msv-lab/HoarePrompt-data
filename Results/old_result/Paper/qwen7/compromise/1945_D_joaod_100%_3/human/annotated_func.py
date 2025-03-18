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
        
    #State: After all iterations of the loop, `total` will hold the minimum cumulative cost from the starting position (`na_frente - 1`) to the end position (`-1`), considering the costs of switching to path `a` or passing through path `b` at each step. The loop iterates backward from `na_frente - 1` to `-1`, updating `total` based on the minimum cost option at each step. The variable `best` will hold the lowest cumulative cost found during the entire process.
#Overall this is what the function does:The function processes multiple test cases, each involving two paths represented by lists `a` and `b`. For each test case, it calculates the minimum cumulative cost to travel from a starting position to an ending position, considering the costs of switching to path `a` or passing through path `b` at each step. It prints the minimum cumulative cost for each test case.

