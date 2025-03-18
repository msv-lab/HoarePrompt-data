#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100. a is a list of n integers such that 1 <= a_i <= 100 for all i in range n.
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
    #- `greater_count` will be the total number of elements in each list `a` that are greater than `favorite_value` across all iterations.
    #- `same_value_count` will be the total number of elements in each list `a` that match `favorite_value` across all iterations.
    #- `n` will retain its initial value, which is the integer value of the first input provided at the start.
    #- `f` will retain its initial value, which is the integer value of the second input provided at the start.
    #- `k` will retain its initial value, which is the integer value of the third input provided at the start.
    #- `favorite_value` will be the element at index `f - 1` in the list `a` from the last iteration.
    #- For each iteration, if `greater_count` is greater than or equal to `k`, the output will be 'YES'. If `greater_count + same_value_count` is greater than `k`, the output will be 'NO'. Otherwise, the output will be 'MAYBE'.
    #
    #This final state reflects the cumulative results of all iterations through the loop based on the given conditions.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n, f, k, and a list a of n integers. It determines whether there are enough elements in the list a that are either greater than or equal to the favorite value (the element at index f-1) to satisfy the condition specified by k. Based on this determination, it prints 'YES', 'NO', or 'MAYBE' for each test case. The final state of the program includes the cumulative counts of elements greater than and equal to the favorite value across all test cases, while the original values of n, f, k, and the list a are retained from the last test case processed.

