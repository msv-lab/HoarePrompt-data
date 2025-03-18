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
        
    #State: All test cases have been processed and their respective outputs have been printed. The variables `t`, `n`, `a`, and `b` remain unchanged.
#Overall this is what the function does:The function processes a number of test cases, each defined by three integers. For each test case, it calculates and prints a result based on specific conditions involving these integers. The input values remain unchanged after processing.

