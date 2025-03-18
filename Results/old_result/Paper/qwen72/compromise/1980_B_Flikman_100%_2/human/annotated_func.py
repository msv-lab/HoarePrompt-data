#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n, f, and k are integers such that 1 <= f, k <= n <= 100, and a is a list of n integers such that 1 <= a_i <= 100.
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
        
    #State: After the loop executes all `t` iterations, `n`, `f`, and `k` will have been reassigned `t` times, and `a` will have been reassigned `t` times as well. For each iteration, `favorite_value` will be the value of `a[f - 1]`, `sorted_a` will be the sorted version of `a` in descending order, `removed_count` will be the number of occurrences of `favorite_value` in the first `k` elements of `sorted_a`, and `favorite_count` will be the total number of occurrences of `favorite_value` in `sorted_a`. If `removed_count` is equal to `favorite_count` for any iteration, "YES" will be printed. If `removed_count` is 0 for any iteration, "NO" will be printed. Otherwise, "MAYBE" will be printed.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, indicating the number of test cases. For each test case, it reads three integers `n`, `f`, and `k`, and a list `a` of `n` integers. The function then determines if the `f`-th element in `a` (considering 1-based indexing) is among the top `k` largest elements in `a` when sorted in descending order. If all occurrences of this element are within the top `k` largest elements, it prints 'YES'. If none of the occurrences are within the top `k` largest elements, it prints 'NO'. Otherwise, it prints 'MAYBE'. After processing all `t` test cases, the function concludes.

