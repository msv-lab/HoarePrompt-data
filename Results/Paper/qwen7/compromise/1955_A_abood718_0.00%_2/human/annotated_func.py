#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three integers n, a, and b, where 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
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
        
    #State: Output State: The output state will consist of a series of lines, each line containing the result of one of the conditions in the loop. Specifically, for each iteration \(i\):
    #
    #- If \(B \times 2 < C\), the output will be \(A \times B\).
    #- If \(A\) is even and \(B \times 2 \geq C\), the output will be \(\frac{A \times C}{2}\).
    #- Otherwise, the output will be two lines: \(X = \frac{A}{2}\) and \(X \times C + B\).
    #
    #The total number of lines in the output will be equal to the number of test cases specified by `int(input())`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \(n\), \(a\), and \(b\). For each test case, it calculates and prints one of three possible outputs based on the values of \(a\) and \(b\):

- If \(2b < c\), it prints \(a \times b\).
- If \(a\) is even and \(2b \geq c\), it prints \(\frac{a \times c}{2}\).
- Otherwise, it first prints \(X = \frac{a}{2}\) and then prints \(X \times c + b\).

After processing all test cases, the function concludes with no return value, only printing the results to the console.

