#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers satisfying 1 ≤ m ≤ n ≤ 200,000. a_1, a_2, ..., a_n and b_1, b_2, ..., b_n are lists of positive integers where 1 ≤ a_i, b_i ≤ 10^9 for all i. The sum of values of n over all test cases does not exceed 2 × 10^5.
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
        
    #State: All iterations of the loop have been executed, `na_frente` is a non-negative integer, `total` is the sum of the minimum costs accumulated from `custo_pra_trocar_a` and `custo_pra_passar_b` lists based on the conditions specified in the loop for all values of `v` in the range from `na_frente` to `-1`, inclusive. `v` is now 0 (since the loop decrements `v` from `na_frente` to 0). `best` is the lowest possible value of `total + custo_pra_trocar_a[v]` or `total + custo_pra_passar_b[v]` for all `v` in the range from `na_frente` to `pos_final`, inclusive, that is less than or equal to `pos_final`.
#Overall this is what the function does:The function processes multiple test cases, each involving integers n and m, and two lists of positive integers a and b. For each test case, it calculates the minimum cost required to transform a sequence of length n based on given conditions and prints the lowest possible cost for each test case.

