#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, a, and b are integers such that 1 <= n <= 100, 1 <= a <= 30, and 1 <= b <= 30.
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
        
    #State: The output consists of a series of printed values based on the conditions checked in each iteration of the loop. Specifically, for each iteration, it prints either `A * B`, `int(A * C / 2)`, or two values: `A // 2` and `X * C + B` where `X = A // 2`, depending on the values of `A`, `B`, and `C`.
#Overall this is what the function does:The function processes a series of test cases, each defined by three integers `A`, `B`, and `C`. For each test case, it prints a result based on specific conditions: if `B * 2` is less than `C`, it prints `A * B`; if `A` is even, it prints `A * C / 2`; otherwise, it prints `A // 2` followed by `(A // 2) * C + B`.

