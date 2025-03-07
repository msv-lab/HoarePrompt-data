#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100. a is a list of n integers such that 1 <= a_i <= 100 for each i from 0 to n-1.
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
        
    #State: Series of outputs ("YES", "NO", "MAYBE") for each test case, with `t`, `n`, `f`, `k`, and `a` retaining their values from the initial state except within the scope of the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives integers `n`, `f`, `k`, and a list `a` of `n` integers. It then outputs "YES", "NO", or "MAYBE" based on the comparison of the `f`-th element in the original list with the `k`-th element in the sorted list.

