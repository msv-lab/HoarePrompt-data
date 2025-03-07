#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and m are integers where 1 ≤ m ≤ n ≤ 200,000, representing the number of people in the queue and the maximum allowable final position of Kirill, respectively. a_1, a_2, ..., a_n are integers where 1 ≤ a_i ≤ 10^9, and b_1, b_2, ..., b_n are integers where 1 ≤ b_i ≤ 10^9, representing the cost to bribe the i-th person and the cost to bribe each person between positions j and i, respectively. The sum of n over all test cases does not exceed 2 × 10^5.
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
        
    #State: `custos` is a list containing the minimum cost for Kirill to bribe his way to a position no greater than `m` for each of the `t` test cases. The length of `custos` is equal to `x`. The values of `t`, `n`, `m`, `a_values`, `b_values`, and `x` are not directly modified by the loop, but `a_values` and `b_values` are populated from input for each test case.
    for c in custos:
        print(c)
        
    #State: The values of `custos` are printed one by one, and the state of `custos` remains unchanged. The values of `t`, `n`, `m`, `a_values`, `b_values`, and `x` are also unchanged.
#Overall this is what the function does:The function reads multiple test cases, each defined by the number of people in a queue `n`, the maximum allowable final position `m`, and two lists of integers `a` and `b` representing the costs to bribe individuals. It calculates and prints the minimum cost required for Kirill to move to a position no greater than `m` for each test case. The function does not return any values; it only prints the results. After the function concludes, the state of the program includes the printed costs for each test case, and the input variables `t`, `n`, `m`, `a_values`, and `b_values` are not directly modified by the function.

