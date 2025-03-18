#State of the program right berfore the function call: There are t test cases (1 ≤ t ≤ 10^4). For each test case, n is the number of people in the queue excluding Kirill (1 ≤ m ≤ n ≤ 200,000), and m is the maximum allowable final position of Kirill in the queue. a_1, a_2, ..., a_n are the costs Kirill has to pay to swap places with the i-th person (1 ≤ a_i ≤ 10^9). b_1, b_2, ..., b_n are the additional costs Kirill has to pay to each person between the j-th and i-th person during a swap (1 ≤ b_i ≤ 10^9). The sum of all n across all test cases does not exceed 2 * 10^5.
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
        
    #State: After processing all test cases, the program will have printed the minimum total cost for Kirill to reach his desired position or better for each test case. The variables `cases`, `na_frente`, `pos_final`, `custo_pra_trocar_a`, `custo_pra_passar_b`, `total`, and `best` will reflect the state of the last processed test case. Specifically, `cases` will remain unchanged, `na_frente` and `pos_final` will hold the values of the last test case, `custo_pra_trocar_a` and `custo_pra_passar_b` will hold the cost lists of the last test case, `total` will be the total cost accumulated during the processing of the last test case, and `best` will be the minimum cost found for Kirill to reach his desired position or better in the last test case.
#Overall this is what the function does:The function processes multiple test cases, each involving a queue of people and a cost structure for Kirill to move within the queue. For each test case, it calculates and prints the minimum total cost for Kirill to reach a position no greater than a specified maximum allowable final position in the queue.

