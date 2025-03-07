#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000. Each test case consists of three integers n, f, and k such that 1 <= f, k <= n <= 100, followed by a list of n integers a_i where 1 <= a_i <= 100.
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
        
    #State: Output State: All variables outside the loop, including `t`, `_`, `n`, `f`, `k`, `a`, `favorite_value`, `sorted_a`, and `favorite_count`, remain unchanged. The variable `removed_count` retains its final value after all iterations of the loop have completed, which could be any non-negative integer depending on the input data. If `removed_count` equals `favorite_count` for all iterations, the condition `if removed_count == favorite_count:` will be true, and "YES" will be printed for each iteration. If `removed_count` never equals `favorite_count`, the condition `elif removed_count == 0:` will be true, and "NO" will be printed for each iteration. Otherwise, "MAYBE" will be printed for each iteration where `removed_count` does not equal `favorite_count` and `removed_count` is not zero.
    #
    #In summary, the output state after all iterations will reflect the final values of `removed_count` and `favorite_count` based on the input data, with all other variables retaining their initial or intermediate values from the last iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers \( n \), \( f \), and \( k \), and a list of \( n \) integers \( a_i \). For each test case, it checks if the count of the \( f \)-th element in the sorted list of \( a_i \) (in descending order) matches the count of that element in the original list. If the counts match for all iterations, it prints "YES". If the count of the \( f \)-th element is never found in the list, it prints "NO". Otherwise, it prints "MAYBE". The function does not return any value but prints the result for each test case.

