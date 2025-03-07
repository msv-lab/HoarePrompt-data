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
            print(X * C + B)
        
    #State: Output State: The output state will consist of a series of integers printed for each iteration of the loop based on the conditions provided in the loop body. Specifically, for each test case, if \(B \times 2 < C\), it prints \(A \times B\); if \(A\) is even, it prints \(\frac{A \times C}{2}\); otherwise, it prints \(\frac{A}{2} \times C + B\). The number of integers printed will be equal to the number of test cases specified by the first input integer \(t\).
#Overall this is what the function does:The function processes a series of test cases, each consisting of integers \(t\), \(n\), \(a\), and \(b\). For each test case, it reads these integers and calculates one of three possible values based on specific conditions: if \(B \times 2 < C\), it prints \(A \times B\); if \(A\) is even, it prints \(\frac{A \times C}{2}\); otherwise, it prints \(\frac{A}{2} \times C + B\). After processing all test cases, the function outputs a series of integers corresponding to the calculated values for each test case.

