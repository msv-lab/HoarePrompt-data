#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and m are integers where 1 ≤ m ≤ n ≤ 200,000, representing the number of people in the queue and the maximum allowable final position of Kirill, respectively. a_i and b_i are lists of integers of length n, where 1 ≤ a_i, b_i ≤ 10^9, representing the cost to bribe the person at position i and the cost to bribe each person between positions j and i, respectively. The sum of n across all test cases does not exceed 2 * 10^5.
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
        
    #State: After all iterations, `t` is an integer where 1 ≤ t ≤ 10^4, `cases` is the same as `t`, `c` is `t-1`, `na_frente` is the last input integer - 1 and must be at least 0, `pos_final` is the last input integer - 1, `custo_pra_trocar_a` is a list of integers read from input, `custo_pra_passar_b` is a new list of integers read from input, `v` is -1, `total` is the sum of the minimum costs (`custo_pra_trocar_a[v]` or `custo_pra_passar_b[v]`) for each iteration from `na_frente` down to 0, and `best` is the lowest value of `total + custo_pra_trocar_a[v]` encountered during the loop, where `v` is less than or equal to `pos_final`.
#Overall this is what the function does:The function processes multiple test cases, each involving a queue of people and the costs associated with bribing them. It calculates the minimum cost for Kirill to move to a position no greater than a specified maximum allowable position within the queue. For each test case, the function outputs the minimum cost required to achieve this goal. After processing all test cases, the function completes without returning any value, and the final state includes the processed test cases and their respective minimum costs printed to the console.

