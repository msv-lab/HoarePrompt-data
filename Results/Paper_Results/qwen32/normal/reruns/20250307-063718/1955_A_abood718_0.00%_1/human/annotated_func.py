#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
def func():
    for i in range(int(input())):
        A, B, C = map(int, input().split())
        
        if B * 2 < C:
            print(A * B)
        elif A % 2 == 0:
            print(int(A * C / 2))
        else:
            X = A // 2
            print(X)
            print(X * C + B)
        
    #State: The loop will have printed the results for each of the `t` test cases based on the conditions provided. The state of `t`, `n`, `a`, and `b` remains unchanged.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers. For each test case, it calculates and prints a result based on specific conditions involving the integers. The final state of the program is that it has printed the results for all test cases, without altering the input values.

