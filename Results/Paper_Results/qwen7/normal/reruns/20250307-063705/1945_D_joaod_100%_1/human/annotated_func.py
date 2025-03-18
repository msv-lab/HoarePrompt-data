#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers satisfying 1 ≤ m ≤ n ≤ 200,000. a and b are lists of n positive integers where 1 ≤ a_i, b_i ≤ 10^9 for all 1 ≤ i ≤ n.
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
        
    #State: All iterations of the loop have been executed. The variable `best` contains the minimum cumulative cost found during the loop, representing the optimal solution for all given inputs. The variable `cases` remains a positive integer within the range 1 ≤ cases ≤ 10^4, `c` is equal to `cases - 1`, `na_frente` and `pos_final` are adjusted according to the loop's decrement, and `custo_pra_trocar_a` and `custo_pra_passar_b` are lists of integers created from the input split. The variable `total` holds the final accumulated cost as per the loop's logic, reflecting the best possible total cost for all inputs.
#Overall this is what the function does:The function processes multiple test cases, where for each case, it calculates the minimum cumulative cost required to transform a sequence of integers represented by list `a` into another sequence represented by list `b`. It achieves this by considering two options at each position: either to change the element in `a` to match the corresponding element in `b` or to pass over the element in `a`. The function outputs the minimum cost for each test case.

