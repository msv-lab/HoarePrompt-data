#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, a, and b are integers such that 1 <= n <= 100 and 1 <= a, b <= 30.
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
        
    #State: a series of printed values based on the conditions for each test case, with variables t, n, a, and b unchanged.
#Overall this is what the function does:The function processes a series of test cases, each defined by three integers. For each test case, it prints a value based on specific conditions involving the integers. The integers representing the number of test cases and the values for each test case remain unchanged after the function executes.

