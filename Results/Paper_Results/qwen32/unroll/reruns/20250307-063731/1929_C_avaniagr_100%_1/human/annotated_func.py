#State of the program right berfore the function call: Each test case consists of three integers k, x, and a, where 2 ≤ k ≤ 30, 1 ≤ x ≤ 100, and 1 ≤ a ≤ 10^9. The number of test cases t satisfies 1 ≤ t ≤ 1000.
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
        
    #State: A sequence of "YES" or "NO" for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers `k`, `x`, and `a`. For each test case, it determines whether a certain condition is met based on the values of `k`, `x`, and `a`, and prints "YES" if the condition is satisfied or "NO" otherwise.

