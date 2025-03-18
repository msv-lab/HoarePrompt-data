#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, k is an integer such that 2 <= k <= 30, x is an integer such that 1 <= x <= 100, and a is an integer such that 1 <= a <= 10^9.
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
        
    #State: Output State: The output state will consist of 'YES' or 'NO' printed for each iteration of the loop based on the conditions provided within the loop. Specifically, it will depend on the values of `k`, `x`, and `a` entered during each iteration, with `t` indicating the number of iterations. Each line of output will either be 'YES' or 'NO', depending on whether the conditions in the loop are met for the given inputs.
#Overall this is what the function does:The function processes a series of inputs (t, k, x, a) where t is the number of iterations, k and x are integers, and a is a large integer. For each iteration, it checks specific conditions involving k, x, and a. If the conditions are met, it prints 'YES'; otherwise, it prints 'NO'. The final state of the program consists of 'YES' or 'NO' outputs for each iteration, based on the evaluated conditions.

