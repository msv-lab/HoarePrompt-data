#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000. For each test case, n, f, and k are positive integers such that 1 <= f, k <= n <= 100. a is a list of n integers such that 1 <= a_i <= 100 for all i in range(n).
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
        
    #State: Output State: The output state will consist of a series of 'YES', 'NO', or 'MAYBE' based on the conditions evaluated for each iteration of the loop. For each iteration, the loop processes an integer `t` (1 to 1000), followed by `t` sets of data. Each set includes integers `n`, `f`, and `k`, and a list `a` of `n` integers. The loop calculates the favorite value (the `f`-th element in the list `a`), counts how many elements are equal to the favorite value (`same_value_count`), and counts how many elements are greater than the favorite value (`greater_count`). Based on these counts, it prints 'YES', 'NO', or 'MAYBE' depending on whether there are at least `k` elements greater than the favorite value or if the sum of elements equal to and greater than the favorite value is less than or equal to `k`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `f`, and `k`, and a list `a` of `n` integers. For each test case, it determines the `f`-th element in the list `a` as the favorite value. It then counts how many elements in the list are equal to the favorite value and how many are greater than the favorite value. Based on these counts, the function prints either 'YES', 'NO', or 'MAYBE' for each test case.

