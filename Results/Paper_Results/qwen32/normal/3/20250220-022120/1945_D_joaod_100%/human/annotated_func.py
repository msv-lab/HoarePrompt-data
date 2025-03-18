#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, for each test case n and m are integers such that 1 <= m <= n <= 200,000, a is a list of n integers where each element a_i satisfies 1 <= a_i <= 10^9, b is a list of n integers where each element b_i satisfies 1 <= b_i <= 10^9, and the sum of all n values across all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `cases` is greater than or equal to 1, `c` is equal to `cases`, and the loop has processed all `cases` test cases. Each test case has computed and printed the minimum total cost (`best`) required to reach the final position from the starting position, considering the costs of switching and passing at each position.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `m` and two lists `a` and `b` of length `n`. For each test case, it calculates and prints the minimum total cost required to reach position `m` from position `1`, considering the costs specified in lists `a` (for switching) and `b` (for passing) at each position.

