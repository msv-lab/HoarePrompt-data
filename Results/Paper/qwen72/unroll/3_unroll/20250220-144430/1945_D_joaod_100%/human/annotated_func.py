#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and m are integers such that 1 ≤ m ≤ n ≤ 200,000, a is a list of integers of length n such that 1 ≤ a_i ≤ 10^9, b is a list of integers of length n such that 1 ≤ b_i ≤ 10^9, and the sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop iterates through each test case, and for each case, it calculates the minimum cost to move an item from the front to the final position, updating the `best` variable with the lowest cost found. After all iterations, the `best` variable contains the minimum cost for the last test case, and the loop prints this value. The variables `t`, `n`, `m`, `a`, `b`, and `cases` remain unchanged.
#Overall this is what the function does:The function `func` reads multiple test cases from the input. For each test case, it calculates the minimum cost to move an item from a specified initial position to a final position, considering two different cost lists. The function prints the minimum cost for each test case. The variables `t`, `n`, `m`, `a`, and `b` are not modified by the function, and the function does not return any value.

