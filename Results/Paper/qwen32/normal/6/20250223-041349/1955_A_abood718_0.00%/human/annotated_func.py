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
        
    #State: The loop has executed `n` times, where `n` is the integer provided as input. For each of these iterations, the loop reads three integers `A`, `B`, and `C` from the input. Depending on the values of `A`, `B`, and `C`, it prints specific values as follows:
    #- If `B * 2 < C`, it prints `A * B`.
    #- If `B * 2` is not less than `C` and `A` is even, it prints `A * C / 2`.
    #- If `B * 2` is not less than `C` and `A` is odd, it prints `A // 2` followed by `(A // 2) * C + B`.
#Overall this is what the function does:The function processes a series of test cases, each defined by three integers `A`, `B`, and `C`. For each test case, it prints a result based on the conditions involving these integers. Specifically, it prints `A * B` if `B * 2` is less than `C`. If `B * 2` is not less than `C` and `A` is even, it prints `A * C / 2`. If `B * 2` is not less than `C` and `A` is odd, it prints `A // 2` followed by `(A // 2) * C + B`.

