#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 1000) representing the number of test cases. Each test case consists of three integers n, m, and k (1 ≤ m, k ≤ n ≤ 50) where n is the number of parts of the ribbon, m is the number of colors available, and k is the maximum number of parts Bob can repaint.
def func():
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) < k:
            print('NO')
        else:
            print('Yes')
        
    #State: a sequence of t lines, each containing either 'NO' or 'YES', based on the input values for each test case.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `n`, `m`, and `k`. For each test case, it determines whether it is possible to repaint up to `k` parts of a ribbon with `n` parts using `m` colors, under the condition that not all parts are repainted and the number of parts not repainted is at least the ceiling of `n` divided by `m`. It outputs 'YES' if the condition is met and 'NO' otherwise.

