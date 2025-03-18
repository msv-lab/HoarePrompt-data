#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100, and a is a list of n integers where each element a_i satisfies 1 <= a_i <= 100.
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
        
    #State: The loop has executed `t` times, where `t` is the initial integer input representing the number of test cases. For each test case, the program has read integers `n`, `f`, and `k`, and a list `a` of `n` integers. The variable `f` and `k` are adjusted by subtracting 1 from each. The list `a` is sorted in descending order, and `x` is assigned the value of `a[f]`. The program then compares `a[k]` with `x` and prints 'NO' if `a[k]` is greater than `x`, 'YES' if `a[k]` is less than `x`, and 'YES' if `a[k]` is equal to `x` and `k` is the last index or `a[k-1]` is less than `x`; otherwise, it prints 'MAYBE'. The state of `t`, `n`, `f`, `k`, `a`, and `x` changes for each iteration based on the input values of each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `f`, `k`, and a list `a` of `n` integers. For each test case, it evaluates the relationship between the element at index `f` in the original list and the element at index `k` in the sorted (descending) list. It prints 'NO' if the element at index `k` in the sorted list is greater than the element at index `f` in the original list, 'YES' if it is less, and 'YES' or 'MAYBE' if they are equal, depending on whether `k` is the last index or the previous element in the sorted list is less than the element at index `f`.

