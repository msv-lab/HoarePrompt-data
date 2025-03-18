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
        
    #State: Output State: The output state consists of `cases` lines, each containing the minimum cost (`best`) found for each test case after executing the given loop. Each test case's result is calculated based on the values of `na_frente`, `pos_final`, `custo_pra_trocar_a`, and `custo_pra_passar_b` for that specific case.
#Overall this is what the function does:The function processes multiple test cases, where for each case, it calculates the minimum cost required to move from position `na_frente` to position `pos_final`. It considers two options for moving: either by changing the value at the current position (with a cost from the `custo_pra_trocar_a` list) or by passing to the next position (with a cost from the `custo_pra_passar_b` list). The function outputs the minimum cost for each test case.

