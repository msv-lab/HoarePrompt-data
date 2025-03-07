#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10⁴, and for each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
def func():
    for i in range(int(input())):
        A, B, C = map(int, input().split())
        
        if B * 2 < C:
            print(A * B)
        elif A % 2 == 0:
            print(int(A * C / 2))
        else:
            X = A // 2
            print(X * C + B)
        
    #State: t is an integer such that 1 ≤ t ≤ 10⁴, and for each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30. The loop variable i will be equal to t after the loop completes. A, B, and C will not hold specific values as they are re-assigned in each iteration.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `A`, `B`, and `C`. For each test case, it prints a calculated value based on specific conditions involving these integers. The final state of the program is that it has printed the result for each of the `t` test cases.

