#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers satisfying 1 ≤ m ≤ n ≤ 200,000. a and b are lists of n positive integers where 1 ≤ a_i, b_i ≤ 10^9 for all 1 ≤ i ≤ n.
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
        
    #State: Output State: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `x` is an input integer, `custos` is a list containing the sum of selected values from arrays `a` and `b` based on specific conditions for each iteration of the loop.
    for c in custos:
        print(c)
        
    #State: The output state will consist of each value in the list `custos`, printed on a new line.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \(m\), \(n\), and two lists of integers \(a\) and \(b\). For each test case, it calculates a cost based on specific conditions involving elements from \(a\) and \(b\). These costs are then stored in a list `custos`. Finally, the function prints each cost in `custos` on a new line.

