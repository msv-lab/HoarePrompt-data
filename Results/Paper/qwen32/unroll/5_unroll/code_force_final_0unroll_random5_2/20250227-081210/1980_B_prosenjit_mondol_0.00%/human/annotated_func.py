#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100. a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 100.
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
        
    #State: n, f, k, and a will reflect the values from the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `f`, `k`, and a list `a` of `n` integers. For each test case, it determines and prints a result ('YES', 'NO', or 'MAYBE') based on the comparison of the `f`-th and `k`-th elements of the sorted list `a`.

