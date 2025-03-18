#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. Each test case consists of three positive integers n, m, and k such that 1 ≤ m, k ≤ n ≤ 50.
def func():
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) < k:
            print('NO')
        else:
            print('Yes')
        
    #State: t is an integer between 1 and 1000 inclusive, itest equals the total number of iterations specified by t, n, m, and k are integers obtained from the input split for each iteration.
#Overall this is what the function does:The function processes up to 1000 test cases, each consisting of three positive integers \(n\), \(m\), and \(k\) where \(1 \leq m, k \leq n \leq 50\). For each test case, it checks if \(n \leq k\) or if \(n - \text{ceil}(n/m) < k\). If either condition is true, it prints 'NO'; otherwise, it prints 'YES'. After processing all test cases, the function concludes.

