#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case consists of two integers n and m where 1 ≤ m ≤ n ≤ 200,000, representing the number of people in the queue and the maximum allowable final position of Kirill, respectively. a is a list of n integers where 1 ≤ a_i ≤ 10^9, representing the cost to bribe the i-th person to move to the front. b is a list of n integers where 1 ≤ b_i ≤ 10^9, representing the cost to bribe each person between positions j and i when Kirill moves from position i to j. The sum of n over all test cases does not exceed 2 × 10^5.
def func():
    x = int(input())
    custos = []
    for i in range(x):
        custo = 0
        
        num_fila = 0
        
        max_p = 0
        
        a_values = []
        
        b_values = []
        
        nf = input().split()
        
        num_fila = int(nf[0])
        
        max_p = int(nf[1])
        
        a = input().split()
        
        b = input().split()
        
        for y in a:
            a_values.append(int(y))
        
        for y in b:
            b_values.append(int(y))
        
        for y in range(num_fila - 1, max_p - 1, -1):
            if a_values[y] < b_values[y]:
                custo += a_values[y]
            else:
                custo += b_values[y]
        
        for y in range(max_p - 1, 0, -1):
            if a_values[y - 1] + b_values[y] <= a_values[y]:
                custo += b_values[y]
                if y == 1:
                    custo += a_values[0]
                    break
            else:
                custo += a_values[y]
                break
        
        custos.append(custo)
        
    #State: `custos` is a list of `t` integers, each representing the minimum cost for Kirill to move to a position no greater than `m` in the corresponding test case. The values of `t`, `n`, `m`, `a`, and `b` remain unchanged.
    for c in custos:
        print(c)
        
    #State: The values of `t`, `n`, `m`, `a`, and `b` remain unchanged. The loop has printed each integer in the list `custos` exactly once, in the order they appear in the list.
#Overall this is what the function does:The function reads a series of test cases, each defined by the number of people in a queue (`n`), the maximum allowable final position for Kirill (`m`), and two lists of integers (`a` and `b`) representing the costs to bribe people. For each test case, it calculates the minimum cost for Kirill to move to a position no greater than `m` and stores these costs in a list `custos`. After processing all test cases, the function prints each cost in `custos` exactly once, in the order they were calculated. The function does not return any value; it only prints the results. The values of `t`, `n`, `m`, `a`, and `b` remain unchanged after the function execution.

