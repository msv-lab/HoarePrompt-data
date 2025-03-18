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
        
    #State: Output State: The loop has completed all its iterations, so the variable `i` will be equal to `t`. The variables `A`, `B`, and `C` will be the values of the last input set during the loop's final iteration. If the condition `B * 2 < C` was met for the last iteration, and `A` was odd, `X` will be set to `A // 2` and printed. Otherwise, `X` will not be defined or will remain from previous iterations if it was printed before. All other variables and their states will remain as they were in the initial or previous states within the loop, unaffected by the loop's completion.
    #
    #In simpler terms, after all iterations, `i` will be `t`, `A`, `B`, and `C` will be the values from the last input, and `X` (if printed) will be the result of the last odd `A` division by 2.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \(A\), \(B\), and \(C\). It prints a result based on specific conditions involving these integers. Specifically, if \(B \times 2 < C\), it prints \(A \times B\). If \(A\) is even, it prints \(\frac{A \times C}{2}\). If \(A\) is odd, it calculates \(\frac{A}{2}\), prints it, and then prints \(\frac{A}{2} \times C + B\). After processing all test cases, the function outputs the final values of \(A\), \(B\), and \(C\) from the last test case, along with any previously printed intermediate results.

