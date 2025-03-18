#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, each test case consists of n, f, and k as integers where 1 <= f, k <= n <= 100, and a list of n integers a_i where 1 <= a_i <= 100.
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
        
    #State: `t` is an integer such that 1 <= t <= 1000, `_` is `t - 1`, `n` is the first integer from the last input, `f` is the second integer from the last input minus 1, `k` is the third integer from the last input minus 1, `a` is a list of integers from the last input sorted in descending order, `x` is the integer at index `f` in the sorted list `a`. If `a[k]` is greater than `x`, then the output is `NO`. If `a[k]` is less than `x`, then the output is `YES`. If `a[k]` is equal to `x`, then the output is `YES` if `k` is the last index of the list or `a[k + 1]` is less than `x`; otherwise, the output is `MAYBE`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `f`, and `k`, and a list of `n` integers `a_i`. For each test case, it determines the relationship between the `f`-th element (0-indexed) of the original list and the `k`-th element (0-indexed) of the sorted list in descending order. The function prints 'NO' if the `k`-th element in the sorted list is greater than the `f`-th element in the original list, 'YES' if it is less, and 'MAYBE' if they are equal, unless `k` is the last index of the list or the next element in the sorted list is less than the `f`-th element, in which case it prints 'YES'. After processing all test cases, the function concludes without returning any value.

