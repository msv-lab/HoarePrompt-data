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
        
    #State: c is equal to cases, v is -1, total is the accumulated minimum cost from na_frente to 0 in the last test case, best is the minimum total when v was less than or equal to pos_final in the last test case, na_frente and pos_final reflect the last test case's values, custo_pra_trocar_a and custo_pra_passar_b reflect the last test case's values.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `m` and two lists `a` and `b`, each of length `n`. For each test case, it calculates and prints the minimum cost to reach from position `m` to position 0, considering the costs specified in lists `a` and `b`.

