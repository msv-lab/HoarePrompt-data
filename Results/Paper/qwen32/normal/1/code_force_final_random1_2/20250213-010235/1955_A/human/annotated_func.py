#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
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
        
    #State: The loop has processed `n` sets of `(A, B, C)` and printed the corresponding results based on the conditions provided. The variables `t`, `n`, `a`, and `b` remain unchanged.
#Overall this is what the function does:The function processes a series of test cases, each defined by three integers \( A \), \( B \), and \( C \). For each test case, it calculates and prints a result based on specific conditions involving these integers. The input consists of an integer \( t \) indicating the number of test cases, followed by \( t \) lines, each containing three integers \( A \), \( B \), and \( C \). The output is a series of integers, one for each test case, representing the calculated result.

