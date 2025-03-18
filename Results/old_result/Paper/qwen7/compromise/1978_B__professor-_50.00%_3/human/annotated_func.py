#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n, a, and b are positive integers such that 1 ≤ n, a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if b <= a:
            print(n * a)
        elif b - a >= n:
            print(int((2 * b - n + 1) * n / 2))
        else:
            print(int((b - a) / 2 * (b - a + 1) + a * n))
        
    #State: Output State: The output state will consist of a series of integers, each corresponding to the result of one iteration of the loop. The number of integers in the output state will be equal to the value of `t`. Each integer is calculated based on the values of `n`, `a`, and `b` for each test case, following the conditions specified in the loop body.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three positive integers \( n \), \( a \), and \( b \). For each test case, it calculates and prints a result based on the given conditions: if \( b \leq a \), it prints \( n \times a \); if \( b - a \geq n \), it prints the sum of the first \( n \) terms of an arithmetic sequence starting from \( 2b - n + 1 \); otherwise, it prints the sum of an arithmetic sequence from \( a \) to \( b - a \) plus \( a \times n \). The function outputs a series of integers, one for each test case.

