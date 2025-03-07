#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and m are integers where 1 ≤ m ≤ n ≤ 200,000, representing the number of people in the queue and the maximum allowable final position of Kirill, respectively. a is a list of n integers where 1 ≤ a_i ≤ 10^9, and b is a list of n integers where 1 ≤ b_i ≤ 10^9, representing the cost to bribe the i-th person and the cost to bribe each person between the current and target positions, respectively. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop iterates through each test case, and for each test case, it calculates the minimum cost for Kirill to reach his desired final position in the queue. The variable `best` holds the minimum cost for the current test case, and this value is printed for each test case. After all test cases are processed, the loop ends, and no changes are made to the variables `t` or `cases`.
#Overall this is what the function does:The function processes multiple test cases, each involving a queue of people. For each test case, it calculates and prints the minimum cost for Kirill to move to a position no greater than `m` in the queue. The function does not return any value; it only prints the result for each test case. After processing all test cases, the function ends without modifying the input variables or any global state.

