#State of the program right berfore the function call: The function should be called with no arguments, and it is expected to handle input and output internally. The input consists of multiple test cases, where the first line is an integer t (1 ≤ t ≤ 1000) representing the number of test cases. Each of the following t lines contains three integers n, m, and k (1 ≤ m, k ≤ n ≤ 50) representing the number of parts of the ribbon, the number of colors available, and the number of parts Bob can repaint, respectively.
def func():
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) < k:
            print('NO')
        else:
            print('Yes')
        
    #State: The loop will have executed `t` times, and for each test case, the output will either be 'NO' or 'Yes' based on the conditions `n <= k` or `n - math.ceil(n / m) < k`. The values of `t`, `n`, `m`, and `k` will not be directly modified by the loop, but `itest` will have the value `t` after the loop completes.
#Overall this is what the function does:The function `func` accepts no parameters and handles input and output internally. It processes multiple test cases, each defined by the number of parts of a ribbon (`n`), the number of colors available (`m`), and the number of parts Bob can repaint (`k`). For each test case, it checks if it is possible to repaint up to `k` parts of the ribbon such that the number of contiguous parts of the same color can be maximized. If the conditions `n <= k` or `n - math.ceil(n / m) < k` are met, it prints 'NO'; otherwise, it prints 'Yes'. After processing all test cases, the function concludes, and the values of `t`, `n`, `m`, and `k` are no longer relevant.

