#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers satisfying 1 ≤ m ≤ n ≤ 200,000. a_1, a_2, ..., a_n and b_1, b_2, ..., b_n are lists of positive integers where 1 ≤ a_i, b_i ≤ 10^9 for all 1 ≤ i ≤ n. Additionally, the sum of the values of n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: Output State: `na_frente` is an input integer minus 1, `v` is -1 (indicating the loop has completed all its iterations), `c` is 10000 (the value of `cases` minus 1), and `total` holds the accumulated cost based on the conditions specified within the loop. The variable `best` will store the lowest value of `total + custo_pra_trocar_a[v]` when `v <= pos_final` and the condition `custo_pra_trocar_a[v] < custo_pra_passar_b[v]` is met during any iteration of the loop.
    #
    #In simpler terms, after all iterations of the loop, `na_frente` will be the input integer minus 1, `v` will be -1 indicating the loop has completed, `c` will be the original input integer `cases` minus 1, and `total` will contain the minimum cumulative cost calculated by the loop. `best` will hold the lowest cumulative cost found during the loop's execution.
#Overall this is what the function does:The function processes multiple test cases, where each test case includes an integer `t`, two integers `na_frente` and `pos_final`, and two lists `custo_pra_trocar_a` and `custo_pra_passar_b`. It calculates the minimum cumulative cost based on specific conditions and prints the result for each test case. After processing all test cases, the function outputs the lowest cumulative cost found for each case.

