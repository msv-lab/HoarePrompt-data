#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000; for each test case, k, x, and a are integers such that 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9.
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
        
    #State: The loop will have executed `t` times, and for each execution, it will have printed either 'YES' or 'NO' based on the conditions provided. The variables `k`, `x`, and `a` will have been updated according to the user's input for each iteration, but `t` will have been decremented to 0.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `k`, `x`, and `a`. Based on the values of `k` and `x`, it determines if `a` meets or exceeds a certain threshold and prints 'YES' if it does, otherwise 'NO'.

