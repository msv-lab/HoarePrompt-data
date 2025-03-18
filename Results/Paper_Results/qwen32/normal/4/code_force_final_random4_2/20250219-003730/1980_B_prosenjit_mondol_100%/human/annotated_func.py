#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100, and a is a list of n integers such that 1 <= a_i <= 100 for each i from 1 to n.
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
            print('YES' if k == n - 1 or a[k + 1] < x else 'MAYBE')
        
    #State: t is an integer such that 1 <= t <= 1000, and the loop has processed all `t` test cases. For each test case, the program has output either 'YES', 'NO', or 'MAYBE' based on the comparison of `a[k]` and `x` after sorting `a` in descending order. The variables `n`, `f`, `k`, and `a` are not retained after each iteration and are re-initialized for the next test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `f`, `k`, and a list `a` of `n` integers. For each test case, it determines and prints whether the `k`-th largest element in the sorted list is greater than, less than, or potentially equal to the element at index `f` (1-based index), outputting 'YES', 'NO', or 'MAYBE' respectively.

