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
        
    #State: The program has processed all `n` test cases, and for each test case, it has printed the appropriate values based on the given conditions. The variables `t`, `n`, `a`, and `b` remain unchanged.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes three integers `A`, `B`, and `C` as input and prints a result based on specific conditions: if `B * 2` is less than `C`, it prints `A * B`; if `A` is even, it prints `A * C / 2`; otherwise, it prints `A // 2` followed by `X * C + B` where `X` is `A // 2`. After processing all test cases, the function concludes without altering the input values.

