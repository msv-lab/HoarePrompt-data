#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n, f, and k are integers such that 1 ≤ f, k ≤ n ≤ 100, and a is a list of n integers where each element a_i satisfies 1 ≤ a_i ≤ 100.
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
        
    #State: t is 0; n, f, k, a, favorite_value, same_value_count, and greater_count reflect the last test case processed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `f`, and `k`, and a list `a` of `n` integers. For each test case, it determines whether the number of elements in `a` that are greater than the `f`-th element (1-based index) plus the number of elements equal to the `f`-th element is sufficient to meet or exceed `k`. It prints 'YES' if the condition is met, 'NO' if it is not, and 'MAYBE' if the number of greater elements is less than `k` but the sum of greater and equal elements is more than `k`.

