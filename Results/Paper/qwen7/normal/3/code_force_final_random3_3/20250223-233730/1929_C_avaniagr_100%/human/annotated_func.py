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
        
    #State: After all iterations, `k` will be reduced to `k - 4`, `x` will be incremented by 3, and `a` will remain unchanged. The variable `z` will be updated according to the provided rules during each iteration.
#Overall this is what the function does:The function processes input values \(k\), \(x\), and \(a\) from standard input. For each set of values, it checks specific conditions and prints 'YES' or 'NO' based on those conditions. After processing all inputs, the variables \(k\) and \(x\) are modified such that \(k\) is reduced by 4 and \(x\) is increased by 3, while \(a\) remains unchanged. The function does not return any value but modifies the internal state of \(k\) and \(x\) and prints 'YES' or 'NO' for each input set.

