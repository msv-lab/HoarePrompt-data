#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n, f, k are integers such that 1 <= f, k <= n <= 100, and a is a list of n integers where 1 <= a_i <= 100.
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
        
    #State: The loop has executed all iterations, and the values of t, n, f, k, and a have been processed according to the loop logic. For each iteration, the value of `x` is set to `a[f]` before sorting `a` in descending order. The loop then checks if `a[k]` is greater than, less than, or equal to `x` and prints 'NO', 'YES', or 'MAYBE' accordingly. After all iterations, the values of t, n, f, k, and a are no longer relevant as they are redefined in each iteration. The final output state is the sequence of 'NO', 'YES', or 'MAYBE' printed for each iteration.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads the values of `n`, `f`, and `k` (integers), and a list `a` of `n` integers. It then checks if the element at index `f-1` in the original list `a` is greater than, less than, or equal to the element at index `k-1` in the sorted list `a` (in descending order). If the element in the sorted list is greater, it prints 'NO'. If it is less, it prints 'YES'. If they are equal, it prints 'YES' if `k` is the last index of the sorted list or if the element before `k` in the sorted list is less than the original element; otherwise, it prints 'MAYBE'. After processing all test cases, the function has no return value, and the final state is a sequence of 'NO', 'YES', or 'MAYBE' printed for each test case.

