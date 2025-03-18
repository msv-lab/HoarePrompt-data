#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n, f, and k are integers for each test case where 1 <= f, k <= n <= 100, and a is a list of n integers where 1 <= a_i <= 100 for each i.
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
        
    #State: The loop has finished executing for all t test cases. For each test case, the variables n, f, k, a, favorite_value, sorted_a, and removed_count have been updated and used to determine the output ('YES', 'NO', or 'MAYBE'). The values of these variables are not retained between test cases, so they will be reset for each new test case. The initial state of t remains unchanged, and the loop has executed t times.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `f`, `k`, and a list `a` of `n` integers. For each test case, it determines whether the `k` largest values in the list `a` include all occurrences of the value at index `f-1` (the "favorite value"). If all occurrences of the favorite value are among the `k` largest values, it prints 'YES'. If none of the `k` largest values are the favorite value, it prints 'NO'. If some but not all occurrences of the favorite value are among the `k` largest values, it prints 'MAYBE'. The function does not return any values, but it prints the result for each test case. The initial state of `t` remains unchanged, and the function processes `t` test cases in total.

