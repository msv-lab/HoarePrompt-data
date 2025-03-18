#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 1000) representing the number of test cases. For each test case, it receives three integers n, m, and k (1 ≤ m, k ≤ n ≤ 50) representing the number of parts of the ribbon, the number of colors available, and the maximum number of parts Bob can repaint, respectively.
def func():
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) < k:
            print('NO')
        else:
            print('Yes')
        
    #State: A series of 'YES' and 'NO' printed for each test case based on the provided conditions.
#Overall this is what the function does:The function processes multiple test cases, each defined by three integers `n`, `m`, and `k`. For each test case, it determines whether it's possible to repaint up to `k` parts of a ribbon divided into `n` parts using `m` colors, under the condition that not all parts are repainted and the remaining unpainted parts are not all of the same color. It outputs 'YES' if the condition is met and 'NO' otherwise.

