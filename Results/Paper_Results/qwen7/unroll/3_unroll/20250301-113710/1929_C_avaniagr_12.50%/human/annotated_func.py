#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, k is an integer such that 2 ≤ k ≤ 30, x is an integer such that 1 ≤ x ≤ 100, and a is an integer such that 1 ≤ a ≤ 10^9.
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
        
    #State: Output State: The output state depends on the inputs provided during each iteration of the loop. For each iteration, the values of `k`, `x`, and `a` are used to determine whether the output will be 'YES' or 'NO'. The value of `t` specifies the number of iterations. After all iterations, the final output will consist of 'YES' or 'NO' printed for each iteration, based on the conditions specified in the loop body.
#Overall this is what the function does:The function processes a series of inputs where `t` specifies the number of iterations. For each iteration, it reads three integers `k`, `x`, and `a`. Based on the values of `k`, `x`, and `a`, it determines whether to print 'YES' or 'NO'. Specifically, if `x < k - 1` and `a` is greater than or equal to `x + 1`, or if `x == k - 1` and `a` is greater than or equal to `x + 3`, it prints 'YES'; otherwise, it prints 'NO'. After processing all iterations, the function concludes without returning any value.

