#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, a, and b are integers such that 1 <= n <= 100 and 1 <= a, b <= 30.
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
        
    #State: The loop variable `i` will be equal to `t`, and for each of the `t` iterations, the values of `A`, `B`, and `C` will have been read and processed, leading to specific printed outputs based on the conditions provided.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `A`, `B`, and `C`. For each test case, it prints a specific result based on the conditions: if `B * 2` is less than `C`, it prints `A * B`; if `A` is even, it prints `A * C / 2`; otherwise, it prints `A // 2` followed by `X * C + B` where `X` is `A // 2`.

