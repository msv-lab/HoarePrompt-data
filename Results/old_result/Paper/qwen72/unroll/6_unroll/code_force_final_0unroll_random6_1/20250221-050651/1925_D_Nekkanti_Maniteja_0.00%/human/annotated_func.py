#State of the program right berfore the function call: The function `func` is not properly defined to solve the given problem. It should accept parameters for the number of test cases, the number of children, the number of friend pairs, the number of excursions, and the list of friend pairs with their initial friendship values. The correct function definition should be:
def func():
    for i in range(int(input())):
        n, m, k = map(int, input().split())
        
        M = 10 ** 9 + 7
        
        c = pow(n * (n - 1) // 1, -1, M)
        
        s = 0
        
        a = 0
        
        for i in range(m):
            u, v, f = map(int, input().split())
            a += f
        
        for i in range(k):
            s = s + c * i * c * m + c * a
        
        print(s % M)
        
    #State: The function will execute the loop for the specified number of test cases, and for each test case, it will calculate the value of `s` based on the inputs and print `s % M`. The variables `n`, `m`, `k`, `M`, `c`, `a`, and `s` will be updated for each test case, but the overall state of the function will reset for each new test case.
#Overall this is what the function does:The function `func` reads input from the user to process multiple test cases. For each test case, it reads the number of children (`n`), the number of friend pairs (`m`), and the number of excursions (`k`). It then calculates a value `s` based on these inputs and the initial friendship values of the friend pairs. The final value of `s` is computed modulo \(10^9 + 7\) and printed. The function does not return any value. The state of the function resets for each new test case, and the variables `n`, `m`, `k`, `M`, `c`, `a`, and `s` are updated accordingly for each test case.

