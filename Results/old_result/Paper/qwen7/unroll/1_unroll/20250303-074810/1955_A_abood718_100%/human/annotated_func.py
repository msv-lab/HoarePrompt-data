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
        
    #State: Output State: The output state will consist of a series of lines, each containing the result of one iteration of the loop based on the given conditions. For each test case, if \(B \times 2 < C\), it prints \(A \times B\); if \(A\) is even, it prints \(\frac{A \times C}{2}\); otherwise, it calculates \(X = \frac{A}{2}\) (integer division) and prints \(X \times C + B\). The number of lines in the output will be equal to the number of test cases specified by the first input integer \(t\).
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads three integers \(A\), \(B\), and \(C\). Based on certain conditions, it calculates and prints a result. If \(B \times 2 < C\), it prints \(A \times B\). If \(A\) is even, it prints \(\frac{A \times C}{2}\). Otherwise, it calculates \(X = \frac{A}{2}\) (integer division) and prints \(X \times C + B\). The function does not return any value but outputs the results for each test case.

