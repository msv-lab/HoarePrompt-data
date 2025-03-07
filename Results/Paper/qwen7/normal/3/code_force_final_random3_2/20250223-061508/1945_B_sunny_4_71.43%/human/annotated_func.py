#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: Output State: The loop has completed all its iterations, so `t` is now 0. For each iteration, `a`, `b`, and `m` were integers entered by the user, and `A` and `B` were calculated as `int(m / a) + 1` and `int(m / b) + 1` respectively. After all iterations, the values of `A` and `B` from the last iteration are printed, and no further inputs or calculations are performed on `a`, `b`, or `m`.
#Overall this is what the function does:The function processes up to 10,000 test cases, each consisting of three integers \(a\), \(b\), and \(m\) (where \(1 \leq a, b, m \leq 10^{18}\)). For each test case, it calculates two values \(A\) and \(B\) as \(A = \text{int}(m / a) + 1\) and \(B = \text{int}(m / b) + 1\). It then prints the sum \(A + B\). After processing all test cases, the function outputs the sum \(A + B\) from the last test case and terminates, leaving no further operations on the input variables.

