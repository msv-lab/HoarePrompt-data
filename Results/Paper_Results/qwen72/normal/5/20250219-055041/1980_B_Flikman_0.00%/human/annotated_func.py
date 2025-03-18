#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100, and a is a list of n integers where 1 <= a_i <= 100.
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
        
    #State: After all iterations of the loop, `t` is reduced to 0, and for each test case, the values of `n`, `f`, and `k` remain unchanged. The list `a` remains the list of integers provided by the user input for each test case. The `favorite_value` is the integer at index `f - 1` in the list `a` for each test case. The `same_value_count` is the number of times the `favorite_value` appears in the list `a` for each test case, and `greater_count` is the number of elements in the list `a` that are greater than `favorite_value` for each test case. For each test case, if `greater_count` is greater than or equal to `k`, the output is 'YES'. If `greater_count + same_value_count` is less than or equal to `k`, the output is 'NO'. If `greater_count + same_value_count` is greater than `k`, the output is 'MAYBE'.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads the input values `n`, `f`, and `k`, and a list `a` of `n` integers. It then determines the value at index `f - 1` in the list `a` and counts how many elements in `a` are equal to or greater than this value. Based on these counts, it prints 'YES' if there are at least `k` elements greater than the value, 'NO' if the sum of elements greater than and equal to the value is less than or equal to `k`, and 'MAYBE' otherwise. The function does not return any value; it only prints the results for each test case. After processing all test cases, the function concludes.

