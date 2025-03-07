#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 1000) representing the number of test cases. Each test case consists of three integers n, m, and k (1 ≤ m, k ≤ n ≤ 50) where n is the number of parts of the ribbon, m is the number of colors, and k is the number of parts Bob can repaint.
def func():
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) < k:
            print('NO')
        else:
            print('Yes')
        
    #State: `itest` is `t-1`, `t` is the number of test cases, and for each test case, the program has printed either 'NO' or 'YES' based on the conditions `n <= k` or `n - math.ceil(n / m) < k`. The values of `n`, `m`, and `k` for each test case have been read from the input and are not altered by the loop.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `n`, `m`, and `k`. It then determines if it is possible to repaint up to `k` parts of a ribbon consisting of `n` parts to make all parts the same color, given `m` colors. It prints 'YES' if it is possible, otherwise 'NO'.

