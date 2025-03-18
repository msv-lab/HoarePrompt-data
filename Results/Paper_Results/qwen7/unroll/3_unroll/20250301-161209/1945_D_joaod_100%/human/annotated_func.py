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
        
    #State: Output State: The value of `t` after all iterations of the loop have finished, with `t` being updated based on the minimum cost calculated for each case provided by the input. For each case, the variable `best` holds the minimum cost to reach `pos_final` from `na_frente`, considering the costs of swapping and passing. After processing all cases, `t` reflects the cumulative effect of these minimum costs across all cases.
#Overall this is what the function does:The function processes multiple test cases, where for each case, it calculates the minimum cost to move from position `na_frente` to position `pos_final` using either swapping or passing, based on given costs. The function updates a variable `best` to store the minimum cost for each case and prints the result for each case. After processing all cases, the function does not return any value but ensures that the minimum cost is printed for each test case.

