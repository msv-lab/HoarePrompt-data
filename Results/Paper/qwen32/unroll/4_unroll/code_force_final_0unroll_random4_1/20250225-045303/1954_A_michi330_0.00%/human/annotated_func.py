#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 1000) representing the number of test cases. Each test case consists of three integers n, m, and k (1 ≤ m, k ≤ n ≤ 50) representing the number of parts of the ribbon, the number of colors available, and the maximum number of parts Bob can repaint, respectively.
def func():
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) < k:
            print('NO')
        else:
            print('Yes')
        
    #State: A sequence of 'YES' or 'NO' strings, one for each test case, corresponding to the result of the condition checks inside the loop.
#Overall this is what the function does:The function processes multiple test cases, each defined by three integers `n`, `m`, and `k`. It determines for each test case whether it is possible to repaint the ribbon under the given constraints and prints 'YES' or 'NO' accordingly.

