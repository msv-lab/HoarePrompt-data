#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and m are integers for each test case such that 1 ≤ m ≤ n ≤ 200,000, a_i and b_i are lists of integers of length n, where 1 ≤ a_i, b_i ≤ 10^9, and the sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `custos` is a list of integers where each integer represents the minimum cost calculated for each test case based on the conditions specified in the loop. The length of `custos` is equal to `x`. The values of `t`, `n`, `m`, `a_i`, `b_i`, and `x` remain unchanged.
    for c in custos:
        print(c)
        
    #State: The values of `t`, `n`, `m`, `a_i`, `b_i`, and `x` remain unchanged. The loop prints each integer in the list `custos` exactly once, in the order they appear in the list. The list `custos` itself remains unchanged.
#Overall this is what the function does:The function `func` reads an integer `x` from the input, which represents the number of test cases. For each test case, it reads two integers `num_fila` and `max_p` and two lists of integers `a_values` and `b_values`. It calculates the minimum cost based on the conditions specified in the loops and appends this cost to the list `custos`. After processing all test cases, it prints each cost in the list `custos` exactly once, in the order they appear. The function does not return any value, and the input variables `t`, `n`, `m`, `a_i`, and `b_i` are not directly used or modified within the function.

