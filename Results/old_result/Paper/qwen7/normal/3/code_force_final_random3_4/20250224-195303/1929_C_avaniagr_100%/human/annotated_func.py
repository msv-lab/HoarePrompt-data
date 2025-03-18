#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, k is an integer such that 2 <= k <= 30, x is an integer such that 1 <= x <= 100, and a is an integer such that 1 <= a <= 10^9.
def func():
    for s in [*open(0)][1:]:
        k, x, a = map(int, s.split())
        
        if x < k - 1:
            if a >= x + 1:
                print('YES')
            else:
                print('NO')
        elif x == k - 1:
            if a >= x + 2:
                print('YES')
            else:
                print('NO')
        else:
            z = k - 2
            for i in range(x - k + 3):
                z += z // (k - 1) + 1
            if a >= z:
                print('YES')
            else:
                print('NO')
        
    #State: t is a positive integer such that \(1 \leq t \leq 1000\), k is the integer value of the first space-separated token from the last line processed by the loop, x is the integer value of the second space-separated token from the last line processed by the loop, a is the integer value of the third space-separated token from the last line processed by the loop, and z is the final value of z after executing the inner loop for \(x - k + 3\) iterations, provided that `a >= z` holds true. If `a < z`, then `a` remains unchanged.
#Overall this is what the function does:The function processes lines of input, each containing three integers \(k\), \(x\), and \(a\). For each line, it checks specific conditions involving \(k\), \(x\), and \(a\) and prints 'YES' or 'NO' based on those conditions. After processing all lines, it does not return any value.

