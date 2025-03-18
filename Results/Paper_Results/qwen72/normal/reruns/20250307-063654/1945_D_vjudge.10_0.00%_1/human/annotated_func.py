#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n and m are integers for each test case where 1 <= m <= n <= 200,000, a_i and b_i are lists of integers of length n where 1 <= a_i, b_i <= 10^9, and the sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: The loop has finished executing all `x` iterations. `custos` is a list containing the final values of `custo` for each iteration, where each `custo` is the sum of the minimum values between `a_values[y]` and `b_values[y]` for all `y` from `num_fila - 1` down to `1`, with adjustments based on the condition `a_values[y - 1] + b_values[y] <= a_values[y]` for `y` from `max_p - 1` down to `1`. The variables `a_values`, `b_values`, `num_fila`, `max_p`, and `custo` are reset and re-evaluated for each iteration, and their final values after the last iteration are not retained.
    for c in custos:
        print(c)
        
    #State: `custos` must be a non-empty list with all elements printed, and the loop has finished executing all iterations.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case is defined by an integer `num_fila` (number of elements in lists `a` and `b`), and an integer `max_p` (a position in the lists). The function reads these values and the lists `a` and `b` from standard input. For each test case, it calculates a cost by summing the minimum values between `a_values[y]` and `b_values[y]` for all `y` from `num_fila - 1` down to `1`, with additional adjustments based on the condition `a_values[y - 1] + b_values[y] <= a_values[y]` for `y` from `max_p - 1` down to `1`. The function then prints the calculated cost for each test case. After processing all test cases, the function ensures that the list `custos` contains the final cost for each test case, and all elements of `custos` are printed. The function does not return any value.

