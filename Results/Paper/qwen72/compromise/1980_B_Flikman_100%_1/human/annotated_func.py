#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 1 <= n <= 100, f and k are integers such that 1 <= f, k <= n, and a is a list of n integers such that 1 <= a_i <= 100.
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
        
    #State: The loop has executed all iterations, and the values of `t`, `n`, `f`, `k`, and `a` have been updated or re-assigned within each iteration. The final values of `t`, `n`, `f`, `k`, and `a` will be the values from the last iteration. The `favorite_value`, `sorted_a`, and `removed_count` variables will be in their final state from the last iteration, but they are not part of the initial state and are recalculated in each iteration. The loop will have printed 'YES', 'NO', or 'MAYBE' for each iteration based on the conditions described in the loop.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `n`, `f`, and `k`, followed by a list `a` of `n` integers. It then checks if the `f`-th element in the list (considering 1-based indexing) is among the top `k` largest elements in the list. If the `f`-th element is present in all `k` largest elements, it prints 'YES'. If the `f`-th element is not present in any of the top `k` largest elements, it prints 'NO'. If the `f`-th element is present in some but not all of the top `k` largest elements, it prints 'MAYBE'. After processing all test cases, the function concludes.

