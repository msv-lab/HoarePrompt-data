#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, n, a, and b are integers such that 1 <= n, a, b <= 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: The loop has finished executing for all test cases, and the values of t, n, a, and b remain unchanged as they are input values for each test case. The loop prints the calculated result for each test case based on the conditions provided.
#Overall this is what the function does:The function `func` processes a series of test cases. It reads an integer `t` from input, which represents the number of test cases. For each test case, it reads three integers `n`, `a`, and `b` from input, where 1 <= n, a, b <= 10^9. The function calculates a value based on the conditions provided and prints the result for each test case. The final state of the program is that all test cases have been processed, and the results have been printed. The input values `t`, `n`, `a`, and `b` remain unchanged as they are read from input for each test case.

