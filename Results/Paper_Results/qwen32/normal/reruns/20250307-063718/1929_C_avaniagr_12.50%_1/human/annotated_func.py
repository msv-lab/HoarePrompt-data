#State of the program right berfore the function call: Each test case consists of three integers k, x, and a, where 2 ≤ k ≤ 30, 1 ≤ x ≤ 100, and 1 ≤ a ≤ 10^9. There are t (1 ≤ t ≤ 1000) such test cases.
def func():
    t = int(input())
    for _ in range(t):
        k, x, a = map(int, input().split())
        
        if x < k - 1:
            if a >= x + 1:
                print('YES')
            else:
                print('NO')
        elif x == k - 1:
            if a >= x + 3:
                print('YES')
            else:
                print('NO')
        else:
            z = 0
            for i in range(x + 1):
                z += z // (k - 1) + 1
            if a >= z:
                print('YES')
            else:
                print('NO')
        
    #State: The output consists of `t` lines, each being either "YES" or "NO" based on the conditions specified for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers `k`, `x`, and `a`. For each test case, it determines whether `a` meets or exceeds a certain threshold based on the values of `k` and `x`, and prints "YES" if it does, otherwise "NO".

