#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 100.
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
        
    #State: a series of 'YES', 'NO', or 'MAYBE' corresponding to each test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives an integer `n` representing the number of elements in a list, an integer `f` indicating the position of a favorite element in the list, and an integer `k`. It also receives a list `a` of `n` integers. The function then determines whether there are at least `k` elements in the list that are greater than the favorite element, or if the total of elements greater than or equal to the favorite element is less than or equal to `k`. Based on these conditions, it prints 'YES', 'NO', or 'MAYBE' for each test case.

