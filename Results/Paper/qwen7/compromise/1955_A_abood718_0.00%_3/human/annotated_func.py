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
            print(X)
            print(X * C + B)
        
    #State: Output State: The output state will consist of a series of lines, each containing either the value of `A * B`, `int(A * C / 2)`, or `X` followed by `X * C + B`, where `X = A // 2`. The number of lines will be equal to the number of test cases specified by the first input integer `t`. Each line's content depends on the values of `A`, `B`, and `C` for each test case, following the conditions given in the loop body.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers A, B, and C. For each test case, it calculates and prints one of three possible values based on specific conditions: A * B, int(A * C / 2), or X followed by X * C + B, where X is defined as A // 2. The function reads the number of test cases from the first input, then iterates through each test case, performing the necessary calculations and printing the results.

