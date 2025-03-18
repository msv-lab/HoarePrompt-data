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
        
    #State: i is equal to n, and t remains unchanged.
#Overall this is what the function does:The function processes multiple test cases, each defined by three integers `A`, `B`, and `C`. For each test case, it calculates and prints a value based on specific conditions involving these integers. The final state of the program is that it has processed all test cases and printed the corresponding results.

