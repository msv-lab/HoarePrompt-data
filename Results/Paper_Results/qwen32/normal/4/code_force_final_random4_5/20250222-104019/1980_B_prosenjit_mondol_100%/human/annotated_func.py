#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100. a is a list of n integers where each element a_i satisfies 1 <= a_i <= 100.
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
        
    #State: The loop will have processed all `t` test cases. For each test case, the program will have determined whether the `k`-th largest element in the sorted list `a` is greater than, less than, or possibly equal to the `f`-th element of the original list `a`. The output for each test case will have been printed as 'NO', 'YES', or 'MAYBE' based on the comparison. The variables `n`, `f`, `k`, and `a` will have been updated for each iteration to reflect the current test case's input values.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives integers `n`, `f`, `k`, and a list `a` of `n` integers. It determines whether the `k`-th largest element in the sorted list `a` is greater than, less than, or possibly equal to the `f`-th element of the original list `a`. It then prints 'NO', 'YES', or 'MAYBE' based on this comparison.

