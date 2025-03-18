#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are positive integers such that 1 ≤ m ≤ n ≤ 200,000; a_1, a_2, ..., a_n and b_1, b_2, ..., b_n are lists of positive integers where 1 ≤ a_i, b_i ≤ 10^9; the sum of the values of n over all test cases does not exceed 2 × 10^5.
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
        
    #State: Output State: `custos` is a list containing the cumulative cost calculated for each test case after executing the loop. Each element in the list represents the final value of `custo` for that specific test case, based on the given inputs `num_fila`, `max_p`, `a_values`, and `b_values`.
    for c in custos:
        print(c)
        
    #State: The output state will be a list containing the same values as the initial state, because the loop does not modify the `custos` list. The `print(c)` statement simply outputs each element of the `custos` list without changing its contents.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of integers \( t \), \( n \), \( m \), and two lists \( a \) and \( b \) of length \( n \). For each test case, it calculates a cumulative cost based on certain conditions involving elements of \( a \) and \( b \). Specifically, it iterates through the lists and sums up values according to predefined rules. After processing all test cases, it prints the cumulative cost for each test case.

