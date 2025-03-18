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
        
    #State: The loop has executed `n` times, printing a value for each iteration based on the conditions involving `A`, `B`, and `C`. The variables `t`, `n`, `a`, and `b` retain their initial values. The variable `X` may have been defined in some iterations but is not relevant to the final output state.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `A`, `B`, and `C`. It then prints a calculated value based on specific conditions involving `A`, `B`, and `C`. After processing all test cases, the function concludes without modifying the input values `t`, `A`, `B`, or `C`.

