#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100. a is a list of n integers such that 1 <= a_i <= 100 for each i from 1 to n.
def func():
    for _ in range(int(input())):
        n, f, k = map(int, input().split())
        
        f -= 1
        
        k -= 1
        
        a = list(map(int, input().split()))
        
        x = a[f]
        
        a.sort(reverse=True)
        
        if a[k] > x:
            print('NO')
        elif a[k] < x:
            print('YES')
        else:
            print('YES' if k == n - 1 or a[k - 1] < x else 'MAYBE')
        
    #State: t iterations have been completed, and for each iteration, the program has read values for n, f, and k, processed a list a of n integers, and printed either 'YES', 'NO', or 'MAYBE' based on the conditions specified.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it receives integers `n`, `f`, and `k`, and a list `a` of `n` integers. It then determines and prints whether the `k`-th largest element in the list is greater than, less than, or potentially equal to the element at index `f` (0-based), printing 'YES', 'NO', or 'MAYBE' accordingly.

