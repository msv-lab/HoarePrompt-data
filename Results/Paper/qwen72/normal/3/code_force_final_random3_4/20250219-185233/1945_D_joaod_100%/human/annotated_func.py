#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and m are integers such that 1 ≤ m ≤ n ≤ 200,000, representing the number of people in the queue and the maximum allowable final position of Kirill, respectively. a is a list of n integers such that 1 ≤ a_i ≤ 10^9, and b is a list of n integers such that 1 ≤ b_i ≤ 10^9, representing the cost to bribe the i-th person and the additional cost to bribe each person between positions j and i, respectively. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `cases` is an input integer greater than 0, `c` is `cases - 1`, `na_frente` is the first integer input by the user minus 1 and must be at least 0, `pos_final` is the second integer input by the user minus 1, `v` is -1, `custo_pra_trocar_a` and `custo_pra_passar_b` are lists of integers input by the user, `total` is the sum of the minimum costs between `custo_pra_trocar_a[v]` and `custo_pra_passar_b[v]` for each `v` from `na_frente` down to 0, and `best` is the minimum total cost of `total + custo_pra_trocar_a[v]` for any `v` that is less than or equal to `pos_final` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by the number of people in the queue (`n`), the maximum allowable final position of Kirill (`m`), the cost to bribe each person (`a`), and the additional cost to bribe each person between positions (`b`). For each test case, it calculates the minimum total cost required for Kirill to move to a position no greater than `m` in the queue and prints this cost. The function does not return any value; it only prints the results. After the function concludes, the state of the program includes `t` (the number of test cases), `cases` (the same as `t`), and `c` (the index of the last test case processed, which is `cases - 1`). The variables `na_frente`, `pos_final`, `custo_pra_trocar_a`, `custo_pra_passar_b`, `total`, and `best` are reset for each test case and are not retained after the function completes.

