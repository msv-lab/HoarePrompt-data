#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
#Overall this is what the function does:The function processes a series of test cases, each defined by three integers `A`, `B`, and `C`. For each test case, it prints a result based on specific conditions: if `B * 2` is less than `C`, it prints `A * B`; if `A` is even, it prints half of `A` multiplied by `C`; otherwise, it prints `A` divided by 2 (integer division), followed by the result of `X * C + B` where `X` is `A` divided by 2.

