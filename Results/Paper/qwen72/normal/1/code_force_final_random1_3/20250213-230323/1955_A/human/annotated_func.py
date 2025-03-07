#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, n, a, and b are integers such that 1 <= n <= 100 and 1 <= a, b <= 30.
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
        
    #State: The loop has completed all its iterations, and `i` is equal to `int(input()) - 1`. The values of `A`, `B`, and `C` are the inputs provided for the last iteration. If `B * 2` is less than `C`, the output is `A * B`. If `B * 2` is greater than or equal to `C`, and if `A` is even, the output is `int(A * C / 2)`. If `B * 2` is greater than or equal to `C` and `A` is odd, the output is `X * C + B`, where `X` is `A // 2`. The total number of iterations is equal to the value of `int(input())`.
#Overall this is what the function does:The function reads a series of test cases from the standard input. For each test case, it takes three integers `A`, `B`, and `C`. Depending on the values of these integers, it prints one of the following results:
- If `B * 2` is less than `C`, it prints `A * B`.
- If `B * 2` is greater than or equal to `C` and `A` is even, it prints `int(A * C / 2)`.
- If `B * 2` is greater than or equal to `C` and `A` is odd, it prints `X * C + B`, where `X` is `A // 2`.

The function processes a total number of test cases equal to the integer value read from the first line of input. After processing all test cases, the function completes and no further state changes occur.

