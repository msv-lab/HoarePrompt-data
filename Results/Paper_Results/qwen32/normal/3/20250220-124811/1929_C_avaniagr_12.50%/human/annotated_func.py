#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. Each of the following t lines contains three integers k, x, and a, where 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9.
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
        
    #State: t is 0; k, x, and a are the values from the last iteration's input.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `k`, `x`, and `a`. It then prints 'YES' if `a` meets or exceeds a certain threshold based on the values of `k` and `x`; otherwise, it prints 'NO'. The final state of the program is that it has processed all `t` test cases and printed the corresponding results.

