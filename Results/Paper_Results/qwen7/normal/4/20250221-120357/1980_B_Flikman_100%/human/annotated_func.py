#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000. For each test case, n, f, and k are positive integers such that 1 <= f, k <= n <= 100. a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 100.
def func():
    t = int(input())
    for _ in range(t):
        n, f, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        favorite_value = a[f - 1]
        
        sorted_a = sorted(a, reverse=True)
        
        removed_count = 0
        
        for i in range(k):
            if sorted_a[i] == favorite_value:
                removed_count += 1
        
        favorite_count = sorted_a.count(favorite_value)
        
        if removed_count == favorite_count:
            print('YES')
        elif removed_count == 0:
            print('NO')
        else:
            print('MAYBE')
        
    #State: Output State: After the loop executes all its iterations, the variable `removed_count` will be equal to the number of times the `favorite_value` appears in the first `k` elements of `sorted_a`, and `favorite_count` will be equal to the total number of times `favorite_value` appears in the entire list `a`. If `removed_count` equals `favorite_count`, the final output will be 'YES'. If `removed_count` is 0, the final output will be 'NO'. Otherwise, the final output will be 'MAYBE'.
    #
    #This means that after all iterations, `removed_count` will reflect how many times the `favorite_value` has been removed from the top `k` elements of the sorted list, and `favorite_count` will show the total occurrences of `favorite_value` in the original list. Based on these counts, the final decision ('YES', 'NO', or 'MAYBE') will be determined as described.
#Overall this is what the function does:The function processes multiple test cases, each defined by a positive integer `t`. For each test case, it reads additional integers `n`, `f`, and `k`, and a list of integers `a`. It then determines whether the `favorite_value` (the element at index `f-1` in `a`) appears in the top `k` elements of the sorted version of `a` as many times as it appears in the entire list `a`. Based on this comparison, it outputs either 'YES', 'NO', or 'MAYBE'.

