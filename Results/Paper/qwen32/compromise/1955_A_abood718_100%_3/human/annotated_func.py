#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three integers n, a, and b where 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three integers n, a, and b where 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers. For each test case, it calculates and prints a value based on specific conditions related to the input integers.

