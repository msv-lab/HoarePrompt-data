#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000. Each test case consists of three integers n, f, and k such that 1 <= f, k <= n <= 100, followed by a list of n integers a_i where 1 <= a_i <= 100.
def func():
    t = int(input())
    for _ in range(t):
        n, f, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        favorite_value = a[f - 1]
        
        same_value_count = 0
        
        for value in a:
            if value == favorite_value:
                same_value_count += 1
        
        greater_count = 0
        
        for value in a:
            if value > favorite_value:
                greater_count += 1
        
        if greater_count >= k:
            print('YES')
        elif greater_count + same_value_count <= k:
            print('NO')
        else:
            print('MAYBE')
        
    #State: Output State: After all iterations of the loop have finished, the following conditions hold:
    #
    #- `greater_count` will be the total number of elements in the list `a` that are greater than `favorite_value` across all iterations.
    #- `same_value_count` will be the total number of times the element at index `f-1` (i.e., `favorite_value`) appears in the list `a` across all iterations.
    #- `favorite_value` will be the element at index `f-1` in the list `a` for each iteration.
    #- `n`, `f`, and `k` will retain their original input values.
    #- `t` will remain unchanged, as it represents the number of iterations.
    #- `_` will be the last index value from the loop, which is `t-1`.
    #- The list `a` will be empty since all its elements have been processed in each iteration.
    #- If `greater_count` is greater than or equal to `k`, the final output will be `'YES'`.
    #- If `greater_count + same_value_count` is less than or equal to `k`, the final output will be `'NO'`.
    #- Otherwise, the final output will be `'MAYBE'`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers \( n \), \( f \), and \( k \), followed by a list of \( n \) integers \( a_i \). For each test case, it determines whether the count of elements greater than the \( f \)-th element in the list plus the count of occurrences of the \( f \)-th element itself is sufficient to meet or exceed \( k \). If the count of greater elements is at least \( k \), it prints 'YES'. If the sum of greater elements and identical elements is less than or equal to \( k \), it prints 'NO'. Otherwise, it prints 'MAYBE'.

