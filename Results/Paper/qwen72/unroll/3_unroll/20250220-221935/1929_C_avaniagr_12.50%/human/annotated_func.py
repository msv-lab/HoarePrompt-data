#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, k, x, and a are integers where 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9.
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
        
    #State: The values of `t`, `k`, `x`, and `a` remain unchanged, but the loop has printed 'YES' or 'NO' for each test case based on the conditions specified in the loop.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `k`, `x`, and `a` from the input. The function then evaluates whether `a` meets certain conditions based on the values of `k` and `x`. If `a` meets the conditions, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function concludes without returning any value, but the input variables `t`, `k`, `x`, and `a` are not retained in their final state.

