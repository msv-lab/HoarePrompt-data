#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 100, f and k are integers such that 1 <= f, k <= n, a is a list of n integers such that 1 <= a_i <= 100.
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
        
    #State: The values of `t`, `n`, `f`, `k`, and `a` remain unchanged after the loop executes all iterations. The loop prints 'YES', 'NO', or 'MAYBE' for each iteration based on the conditions provided in the loop body.
#Overall this is what the function does:The function `func` reads an integer `t` and then, for each of the `t` test cases, it reads three integers `n`, `f`, and `k`, followed by a list `a` of `n` integers. It determines if there are at least `k` integers in `a` that are greater than the integer at index `f-1` in `a`. If there are, it prints 'YES'. If there are fewer than `k` integers greater than the favorite value and the total count of integers equal to or greater than the favorite value is less than or equal to `k`, it prints 'NO'. Otherwise, it prints 'MAYBE'. The function does not return any value.

