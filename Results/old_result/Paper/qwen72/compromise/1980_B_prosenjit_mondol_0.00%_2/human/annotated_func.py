#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 1 <= n <= 100, f and k are integers such that 1 <= f, k <= n, and a is a list of n integers such that 1 <= a_i <= 100.
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
        
    #State: The loop has finished executing all iterations. For each test case, the variable `x` holds the value of `a[f]` before sorting, `a` is sorted in descending order, and the output is either 'YES', 'NO', or 'MAYBE' based on the conditions specified in the loop. The values of `t`, `n`, `f`, `k`, and `a` for the next test case (if any) are undefined and will be determined by the next input.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n`, two integers `f` and `k` (both within the range [1, n]), and a list `a` of `n` integers (each within the range [1, 100]). It then checks if the value at index `f-1` in the original list `a` is greater than, less than, or equal to the value at index `k-1` in the sorted list `a` (in descending order). If the value is greater, it prints 'YES'. If the value is less, it prints 'NO'. If the value is equal, it prints 'YES' if `k` is the last index of the sorted list or if the value at `k-1` in the sorted list is less than the value at `f-1` in the original list; otherwise, it prints 'MAYBE'. After processing all test cases, the function concludes.

