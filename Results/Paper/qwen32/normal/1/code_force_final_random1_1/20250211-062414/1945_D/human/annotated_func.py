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
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4, cases is an integer representing the number of test cases, c is equal to cases, na_frente is the first integer read from the last test case minus 1, pos_final is the second integer read from the last test case minus 1, custo_pra_trocar_a is the list of integers read from the last test case, custo_pra_passar_b is the list of integers read from the last test case, v is -1, total is the accumulated cost based on the minimum costs between custo_pra_trocar_a[v] and custo_pra_passar_b[v] for all v from na_frente down to 0 for the last test case, best is the minimum value of total + custo_pra_trocar_a[v] for all v where v was less than or equal to pos_final for the last test case.
#Overall this is what the function does:The function reads multiple test cases, each consisting of two integers `na_frente` and `pos_final`, and two lists of integers `custo_pra_trocar_a` and `custo_pra_passar_b`. For each test case, it calculates and prints the minimum possible cost to reach `pos_final` from `na_frente` by either passing through elements in `custo_pra_passar_b` or swapping to elements in `custo_pra_trocar_a`.

