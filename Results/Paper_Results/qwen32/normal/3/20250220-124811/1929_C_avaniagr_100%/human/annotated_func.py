#State of the program right berfore the function call: Each test case contains three integers k, x, and a, where 2 ≤ k ≤ 30, 1 ≤ x ≤ 100, and 1 ≤ a ≤ 10^9. There are t test cases, where 1 ≤ t ≤ 1000.
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
        
    #State: The output state after all iterations is determined by the last test case processed. The values of `k`, `x`, and `a` will be those of the last test case, and the output will be "YES" or "NO" based on the conditions of that test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers `k`, `x`, and `a`. For each test case, it determines whether a certain condition is met based on the values of `k`, `x`, and `a`, and prints "YES" if the condition is satisfied or "NO" otherwise. The final state of the program is the output of "YES" or "NO" for each test case, with the output for the last test case being the last printed result.

