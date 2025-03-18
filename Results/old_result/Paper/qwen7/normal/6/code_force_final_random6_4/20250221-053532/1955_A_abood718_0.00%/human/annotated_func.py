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
        
    #State: The loop will continue to execute until all input test cases are processed. After all iterations, `i` will be equal to `t - 1`, where `t` is the total number of test cases. The values of `A`, `B`, and `C` will be updated according to the conditions specified in the loop body. Specifically, if `A` is even, it will be halved; if `A` is odd, it will be halved and then `B * 2 >= C` will hold. The final output will consist of the results printed during each iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each containing three integers A, B, and C. For each test case, it prints one or two values based on specific conditions. If B * 2 is less than C, it prints A * B. If A is even, it prints int(A * C / 2). If A is odd, it prints A // 2 followed by A // 2 * C + B. After processing all test cases, the function concludes without returning any value.

