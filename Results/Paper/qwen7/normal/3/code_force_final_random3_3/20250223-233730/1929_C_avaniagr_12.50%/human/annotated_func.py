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
        
    #State: All variables `k`, `x`, `a`, `t`, `z`, and `i` are reset to their initial values before the loop starts.
#Overall this is what the function does:The function processes multiple test cases (determined by `t`). For each test case, it reads three integers (`k`, `x`, and `a`) and determines whether a certain condition is met based on these inputs. If the condition is satisfied, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function resets all relevant variables to their initial values.

