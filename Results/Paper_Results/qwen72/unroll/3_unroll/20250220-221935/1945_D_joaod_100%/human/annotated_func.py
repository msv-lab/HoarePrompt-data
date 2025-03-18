#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and m are integers such that 1 ≤ m ≤ n ≤ 200,000, representing the number of people in the queue and the maximum allowable final position of Kirill, respectively. a is a list of n integers such that 1 ≤ a_i ≤ 10^9, and b is a list of n integers such that 1 ≤ b_i ≤ 10^9, representing the cost to bribe the i-th person and the cost to bribe each person between positions j and i, respectively. The sum of the values of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop iterates through each test case, and for each test case, it calculates the minimum cost for Kirill to move to a position not greater than `m`. After all iterations, the variable `best` holds the minimum cost for the last test case, and this value is printed. The variables `t`, `cases`, `n`, `m`, `a`, and `b` remain unchanged as they are input values and not modified within the loop.
#Overall this is what the function does:The function reads multiple test cases, each consisting of the number of people in a queue (`n`), the maximum allowable final position of Kirill (`m`), a list of costs to bribe each person in the queue (`a`), and a list of costs to bribe each person between positions (`b`). For each test case, it calculates the minimum cost for Kirill to move to a position no greater than `m` in the queue and prints this cost. The function does not return any value; it only prints the results. After processing all test cases, the input variables remain unchanged.

