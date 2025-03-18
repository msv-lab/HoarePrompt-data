#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 100, f and k are integers such that 1 <= f, k <= n, and a is a list of n integers where 1 <= a_i <= 100.
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
        
    #State: The values of `t`, `n`, `f`, `k`, and `a` are not retained after each iteration of the loop, and the loop will execute `t` times. After all iterations, the variables `t`, `n`, `f`, `k`, and `a` will have their final values as determined by the last iteration of the loop. The list `a` will be sorted in descending order, and the values of `n`, `f`, and `k` will be the last input values for these variables. The value of `t` will be 0 if the loop has completed all its iterations.
#Overall this is what the function does:The function `func` reads `t` test cases from the input, where each test case consists of `n`, `f`, `k`, and a list `a` of `n` integers. For each test case, it checks if the `f`-th element of `a` (0-indexed) is greater than, less than, or equal to the `k`-th element of the sorted list `a` (in descending order). It prints 'NO' if the `f`-th element is greater than the `k`-th element, 'YES' if it is less than or equal to the `k`-th element, and 'MAYBE' if it is equal to the `k`-th element and `k` is not the last index or the element before `k` is less than the `f`-th element. After all test cases, the function does not return any value, and the variables `t`, `n`, `f`, `k`, and `a` will have their final values as determined by the last test case.

