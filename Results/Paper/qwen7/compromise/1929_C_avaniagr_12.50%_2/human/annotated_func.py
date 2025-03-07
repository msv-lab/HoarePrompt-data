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
        
    #State: t is 0, k is an input integer, x is an input integer, a is an input integer, and z is 8.
#Overall this is what the function does:The function processes multiple test cases (up to 1000) where for each case, it takes three integers \(t\), \(k\), and \(x\) and one large integer \(a\). Based on these inputs, it determines whether a certain condition is met and prints 'YES' or 'NO'. Specifically, it checks if \(a\) is sufficiently large compared to a calculated value \(z\), which depends on \(x\) and \(k\). The function does not return any value but prints 'YES' or 'NO' for each test case.

