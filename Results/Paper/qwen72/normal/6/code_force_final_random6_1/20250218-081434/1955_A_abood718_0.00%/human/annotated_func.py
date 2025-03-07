#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, n, a, and b are integers such that 1 <= n <= 100 and 1 <= a, b <= 30.
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
        
    #State: `i` is `int(input()) - 1`, `A`, `B`, and `C` are the integers input by the user, split by spaces. If `B * 2 < C`, there are no changes to the variables. Otherwise, if `A` is even, there are no changes to the variables. If `A` is odd, `X` is set to `A // 2`.
#Overall this is what the function does:The function processes a series of test cases, each defined by three integers `A`, `B`, and `C` provided by the user. For each test case, it prints a result based on the following conditions: if `B * 2 < C`, it prints `A * B`; if `A` is even, it prints `A * C / 2` as an integer; if `A` is odd, it prints `X` (where `X` is `A // 2`) and then prints `X * C + B`. The function does not return any values; it only prints the results for each test case. After the function concludes, the variables `i`, `A`, `B`, and `C` are in the state they were last set to within the loop, and `X` is set to `A // 2` if `A` was odd in the last test case.

