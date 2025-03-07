#State of the program right berfore the function call: t is an integer where 1 <= t <= 1000, n is an integer where 1 <= n <= 100, f and k are integers where 1 <= f, k <= n, and a is a list of n integers where 1 <= a_i <= 100.
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
        
    #State: After all iterations of the loop, `n` retains its initial integer value, `f` and `k` are each decreased by the number of iterations (t), `_` is incremented by the number of iterations (t), `a` is a list of integers input by the user and is sorted in descending order for each iteration, and `x` is the integer value at the index `f` in the sorted list `a` for each iteration. If `a[k]` is greater than `x` for any iteration, then `a[k]` remains greater than `x` for that iteration. If `a[k]` is less than or equal to `x` for any iteration, then `a[k]` is less than or equal to `x` for that iteration.
#Overall this is what the function does:The function processes a series of test cases, each defined by an integer `n`, two integers `f` and `k`, and a list `a` of `n` integers. For each test case, it determines and prints whether the value at index `f-1` in the original list `a` is greater than, less than, or possibly equal to the value at index `k-1` in the sorted (descending order) list `a`. The function does not return any value but prints 'YES', 'NO', or 'MAYBE' for each test case based on the comparison. After processing all test cases, the function concludes, and the input variables `n`, `f`, `k`, and `a` are no longer relevant.

