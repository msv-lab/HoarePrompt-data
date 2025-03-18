#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 1 <= n <= 100, f and k are integers such that 1 <= f, k <= n, and a is a list of n integers such that 1 <= a_i <= 100.
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
        
    #State: The values of `t`, `n`, `f`, `k`, and `a` remain unchanged, but the loop has printed 'YES', 'NO', or 'MAYBE' for each iteration based on the conditions specified in the loop.
#Overall this is what the function does:The function `func` reads input for `t` test cases, where each test case consists of `n`, `f`, and `k` integers, and a list `a` of `n` integers. For each test case, it determines the value at index `f-1` in the list `a` (referred to as the favorite value). It then counts how many values in `a` are equal to the favorite value and how many are greater than the favorite value. Based on these counts, it prints 'YES' if there are at least `k` values greater than the favorite value, 'NO' if the sum of values equal to and greater than the favorite value is less than or equal to `k`, and 'MAYBE' otherwise. The function does not return any values, but it prints the result for each test case.

