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
        
    #State: The loop has executed all its iterations, with `i` being equal to the total number of iterations (which is the same as the number of test cases entered), `A`, `B`, and `C` being the last integers entered by the user for the final test case. The variable `X` is either the integer value of `A` divided by 2 using integer division if `A` was odd in any of the iterations, or it is the integer value of `A` divided by 2 using integer division for the last iteration if `A` was even.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \(A\), \(B\), and \(C\). For each test case, it prints one of three values based on specific conditions involving \(A\) and \(B\). Specifically, if \(B \times 2\) is less than \(C\), it prints \(A \times B\); if \(A\) is even, it prints \(\frac{A \times C}{2}\); otherwise, it calculates \(\frac{A}{2}\) (integer division) and prints the result multiplied by \(C\) plus \(B\). After processing all test cases, the function does not return any value.

