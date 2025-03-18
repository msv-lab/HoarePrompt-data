#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n and m are integers where 1 ≤ m ≤ n ≤ 200,000, a is a list of n integers where 1 ≤ a_i ≤ 10^9, and b is a list of n integers where 1 ≤ b_i ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The variable `cases` is decremented by the number of iterations the loop has run. The variables `na_frente`, `pos_final`, `custo_pra_trocar_a`, `custo_pra_passar_b`, `total`, and `best` are updated based on the input provided during each iteration of the loop. The final value of `best` is printed for each case. The initial values of `t`, `n`, and `m` remain unchanged. The lists `a` and `b` are not modified by the loop.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads two integers `na_frente` and `pos_final`, followed by two lists of integers `custo_pra_trocar_a` and `custo_pra_passar_b`. It then calculates the minimum cost to move from `na_frente` to `pos_final` using the costs provided in the lists. The function prints the minimum cost for each test case. The function does not return any value. The initial values of `t`, `n`, and `m` are not modified, and the lists `a` and `b` are not used within the function.

