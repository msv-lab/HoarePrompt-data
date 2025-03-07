#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, k, x, and a are integers such that 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9.
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
        
    #State: The loop has executed `t` times, where `t` is the number of test cases. For each test case, the program reads integers `k`, `x`, and `a`. It then checks the conditions based on the value of `x` relative to `k` and prints 'YES' or 'NO' accordingly. The values of `k`, `x`, and `a` are reset for each iteration, and the variable `z` is recalculated as needed for each test case.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `k`, `x`, and `a`. It then prints 'YES' or 'NO' based on whether `a` meets or exceeds a certain threshold determined by `k` and `x`.

