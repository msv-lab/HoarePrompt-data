#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100, and a is a list of n integers such that 1 <= a_i <= 100.
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
        
    #State: `t` is an integer such that 1 <= t <= 1000, `n`, `f`, and `k` are integers such that 1 <= f, k <= n <= 100 for each test case, and `a` is a list of integers such that 1 <= a_i <= 100 for each test case. For each iteration, `f` and `k` are decremented by 1, `a` is sorted in descending order, `x` is the integer at index `f` in the sorted list `a`. If `a[k]` is greater than `x`, then "NO" is printed. If `a[k]` is less than `x`, then "YES" is printed. If `a[k]` is equal to `x`, then "YES" is printed if `k` is the last index or the integer at index `k - 1` in the sorted list `a` is less than `x`; otherwise, "MAYBE" is printed.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `f`, and `k`, and a list of integers `a`. For each test case, it checks the relationship between the `f`-th element (0-indexed) of the original list `a` and the `k`-th element (0-indexed) of the sorted list `a` in descending order. If the `k`-th element in the sorted list is greater than the `f`-th element in the original list, it prints "NO". If the `k`-th element in the sorted list is less than the `f`-th element in the original list, it prints "YES". If the `k`-th element in the sorted list is equal to the `f`-th element in the original list, it prints "YES" if `k` is the last index or the element at `k-1` in the sorted list is less than the `f`-th element in the original list; otherwise, it prints "MAYBE". The function does not return any value; it only prints the results for each test case.

