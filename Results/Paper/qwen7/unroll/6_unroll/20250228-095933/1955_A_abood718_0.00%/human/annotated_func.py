#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
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
        
    #State: Output State: The output state will consist of a series of lines, where each line is determined by the values of \(A\), \(B\), and \(C\) for each test case. Specifically:
    #
    #- If \(B \times 2 < C\), the output will be \(A \times B\).
    #- If \(A\) is even, the output will be \(\frac{A \times C}{2}\).
    #- If \(A\) is odd, the output will first print \(X = \frac{A}{2}\) (integer division), followed by \(X \times C + B\).
    #
    #Each test case's output is independent of others, and the total output will be the concatenation of outputs from all test cases.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \(n\), \(a\), and \(b\). For each test case, it calculates and prints one of three possible outputs based on the values of \(a\) and \(b\):
- If \(2b < c\), it prints \(a \times b\).
- If \(a\) is even, it prints \(\frac{a \times c}{2}\).
- If \(a\) is odd, it first prints \(\frac{a}{2}\) (integer division), followed by \(\frac{a}{2} \times c + b\).

After processing all test cases, the function outputs a series of lines, each corresponding to the output of a single test case, without returning any value.

