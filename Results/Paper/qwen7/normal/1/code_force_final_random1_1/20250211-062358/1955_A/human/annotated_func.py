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
        
    #State: Output State: The loop has completed all its iterations, with `i` being equal to the total number of test cases specified by `t`. For each test case, the variables `A`, `B`, and `C` are the integers obtained from the corresponding input. The output of each iteration is determined based on the conditions provided within the loop:
    #
    #- If `B * 2 < C`, the output is `A * B`.
    #- If `B * 2 >= C` and `A` is even, the output is `int(A * C / 2)`.
    #- If `B * 2 >= C` and `A` is odd, the output is `X * C + B`, where `X = A // 2`.
    #
    #All other variables outside the loop, including `t`, remain unchanged from their initial or previous states after the loop completes.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers \(A\), \(B\), and \(C\). For each test case, it calculates and prints one of three possible outputs based on the values of \(A\) and \(B\) relative to \(C\):
- If \(2B < C\), it prints \(A \times B\).
- If \(2B \geq C\) and \(A\) is even, it prints \(\frac{A \times C}{2}\).
- If \(2B \geq C\) and \(A\) is odd, it prints \(\left\lfloor \frac{A}{2} \right\rfloor \times C + B\).

After processing all test cases, the function does not return any value but prints the calculated outputs for each test case.

