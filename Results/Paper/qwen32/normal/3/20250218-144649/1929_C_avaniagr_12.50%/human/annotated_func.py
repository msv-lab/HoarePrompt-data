#State of the program right berfore the function call: Each test case consists of three integers k, x, and a, where 2 ≤ k ≤ 30, 1 ≤ x ≤ 100, and 1 ≤ a ≤ 10^9. There are t test cases, where 1 ≤ t ≤ 1000.
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
        
    #State: The loop has processed all `t` test cases, and the values of `k`, `x`, `a`, and `t` are as they were initially, except `t` is now 0.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `k`, `x`, and `a`. For each test case, it determines whether a certain condition based on these integers is met and prints 'YES' or 'NO' accordingly.

