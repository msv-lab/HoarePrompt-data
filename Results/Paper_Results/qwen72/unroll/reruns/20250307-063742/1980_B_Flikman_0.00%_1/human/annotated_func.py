#State of the program right berfore the function call: t is an integer where 1 <= t <= 1000, n is an integer where 1 <= n <= 100, f and k are integers where 1 <= f, k <= n, and a is a list of n integers where 1 <= a_i <= 100.
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
        
    #State: The values of `t`, `n`, `f`, `k`, and `a` remain unchanged as they are re-assigned within each iteration of the loop. The loop will print 'YES', 'NO', or 'MAYBE' for each iteration based on the conditions provided, but the final state of the variables will be the same as the initial state.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads three integers `n`, `f`, and `k`, and a list `a` of `n` integers. It then checks if the number of elements in `a` that are greater than the value at index `f-1` is at least `k`. If so, it prints 'YES'. If the sum of the number of elements greater than and equal to the value at index `f-1` is less than or equal to `k`, it prints 'NO'. Otherwise, it prints 'MAYBE'. The function does not modify the input variables and does not return any value.

