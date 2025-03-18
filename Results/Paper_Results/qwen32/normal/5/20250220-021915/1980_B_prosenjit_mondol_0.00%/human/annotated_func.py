#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each of the t test cases, n, f, and k are integers such that 1 <= f, k <= n <= 100, and a is a list of n integers where each element a_i satisfies 1 <= a_i <= 100.
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
        
    #State: t
#Overall this is what the function does:The function processes `t` test cases. For each test case, it receives integers `n`, `f`, and `k`, and a list `a` of `n` integers. It then determines and prints whether the element at index `f` in the original list `a` is smaller than, larger than, or possibly equal to the element at index `k` in the list `a` when sorted in descending order.

