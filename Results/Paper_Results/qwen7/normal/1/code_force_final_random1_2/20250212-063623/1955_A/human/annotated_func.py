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
        
    #State: The loop has executed all its iterations, meaning `i` is now equal to `t - 1`. The values of `A`, `B`, and `C` are the last set of inputs provided by the user during the loop's execution. Depending on the conditions within the loop, either `A * B`, `int(A * C / 2)`, or `X * C + B` (where `X = A // 2`) was printed for each iteration. The variable `X` retains its final value after the last iteration based on the conditions evaluated.
#Overall this is what the function does:The function processes a series of test cases, each defined by three integers \(A\), \(B\), and \(C\). For each test case, it prints one of three possible values based on the conditions: \(A \times B\), \(\text{int}(A \times C / 2)\), or \(\text{X} \times C + B\) where \(\text{X} = A // 2\). After processing all test cases, the function does not return any value.

