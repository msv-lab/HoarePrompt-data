#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and m are integers such that 1 <= m <= n <= 200,000. a is a list of n integers where each element a_i satisfies 1 <= a_i <= 10^9. b is a list of n integers where each element b_i satisfies 1 <= b_i <= 10^9. The sum of all n values across all test cases does not exceed 2 * 10^5.
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
        
    #State: `custos` is a list of `x` integers, where each integer is the calculated `custo` for each test case. The other variables (`t`, `n`, `m`, `a`, `b`, `x`) remain unchanged.
    for c in custos:
        print(c)
        
    #State: Each integer in the list `custos` is printed on a new line. The variables `t`, `n`, `m`, `a`, `b`, and `x` remain unchanged.
#Overall this is what the function does:The function reads multiple test cases, each consisting of integers `n` and `m` and two lists `a` and `b` of length `n`. For each test case, it calculates a specific cost based on the values in `a` and `b` and prints this cost. The function does not modify the input values but outputs a computed value for each test case.

