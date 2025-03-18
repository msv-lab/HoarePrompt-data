#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100. a is a list of n integers such that 1 <= a_i <= 100 for each i from 1 to n.
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
        
    #State: The program has processed all `t` test cases and printed the results ('YES', 'NO', or 'MAYBE') for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `f`, and `k`, and a list `a` of `n` integers. For each test case, it determines if the number of elements in `a` that are greater than the element at index `f-1` (the favorite value) is at least `k`, if it is less than `k` but the sum of elements greater than and equal to the favorite value is at most `k`, or neither condition is met. It prints 'YES', 'NO', or 'MAYBE' accordingly for each test case.

