#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000. For each test case, k is an integer such that 2 <= k <= 30, x is a positive integer such that 1 <= x <= 100, and a is a positive integer such that 1 <= a <= 10^9.
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
        
    #State: t is the same as the initial t, k, x, and a are the values read in the last iteration.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads integers `k`, `x`, and `a`. It then determines whether `a` is sufficiently large based on the values of `k` and `x` and prints 'YES' or 'NO' accordingly.

