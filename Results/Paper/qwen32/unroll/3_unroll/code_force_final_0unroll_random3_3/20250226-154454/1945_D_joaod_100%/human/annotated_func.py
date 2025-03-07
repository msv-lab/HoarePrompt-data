#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and m are integers such that 1 <= m <= n <= 200,000. a is a list of n integers where each element a_i satisfies 1 <= a_i <= 10^9. b is a list of n integers where each element b_i satisfies 1 <= b_i <= 10^9. The sum of all n values across all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `cases` is an integer representing the number of test cases; `na_frente` and `pos_final` are the values corresponding to the last test case, with `na_frente` and `pos_final` decremented by 1; `custo_pra_trocar_a` is a list of integers representing the costs to change elements for the last test case; `custo_pra_passar_b` is a list of integers representing the costs to pass through elements for the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `m` (with `m` ≤ `n`), and two lists `a` and `b` of length `n`. For each test case, it calculates and prints the minimum cost to reach a specific position, considering the costs in lists `a` and `b`.

