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
        
    #State: After all iterations of the loop have finished, the value of `t` will be 0, as each iteration decreases `t` by 1 until it reaches 0. The values of `k`, `x`, and `a` will retain their final values from the last iteration of the loop. `i` will be equal to `2x + 1` if `x` was greater than or equal to `k - 1` during the last iteration, otherwise `i` will be equal to `x`. The variable `z` will be the final calculated value based on the conditions met in the last iteration of the loop. If `a` is greater than or equal to `z`, then `a` remains unchanged. If `a` is less than `z`, then `a` is updated to `z`.
#Overall this is what the function does:The function processes a series of inputs where `t` specifies the number of test cases. For each test case, it reads three integers `k`, `x`, and `a`. It then checks specific conditions involving these values and prints 'YES' or 'NO' based on those conditions. After processing all test cases, the function does not return any value but prints the results for each test case.

