#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, k, x, and a are integers such that 2 ≤ k ≤ 30, 1 ≤ x ≤ 100, and 1 ≤ a ≤ 10^9.
def func():
    for s in [*open(0)][1:]:
        k, x, a = map(int, s.split())
        
        if x < k - 1:
            if a >= x + 1:
                print('YES')
            else:
                print('NO')
        elif x == k - 1:
            if a >= x + 2:
                print('YES')
            else:
                print('NO')
        else:
            z = k - 2
            for i in range(x - k + 3):
                z += z // (k - 1) + 1
            if a >= z:
                print('YES')
            else:
                print('NO')
        
    #State: The final output state is determined by the last line of input. The variables `k`, `x`, and `a` will be the values from the last line, and the output will be either "YES" or "NO" based on the conditions specified in the loop.
#Overall this is what the function does:The function reads multiple test cases from the standard input. Each test case consists of three integers: `k`, `x`, and `a`. For each test case, it determines whether `a` meets or exceeds a certain threshold based on the values of `k` and `x`, and prints "YES" if the condition is met or "NO" otherwise.

