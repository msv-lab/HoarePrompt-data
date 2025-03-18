#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100, and a is a list of n integers where each element a_i satisfies 1 <= a_i <= 100.
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
        
    #State: The loop has executed `t` times, and for each execution, it has read integers `n`, `f`, `k`, and a list `a` of `n` integers. It has determined the `favorite_value` as `a[f - 1]`, sorted the list `a` in descending order to get `sorted_a`, and counted how many times `favorite_value` appears in the first `k` elements (`removed_count`) and in the entire `sorted_a` list (`favorite_count`). Depending on the comparison between `removed_count` and `favorite_count`, it has printed 'YES', 'NO', or 'MAYBE'. After all `t` iterations, `t` is reduced to 0, and no more inputs are processed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `f`, `k`, and a list `a` of `n` integers. For each test case, it determines if the `f`-th element in the list `a` (referred to as `favorite_value`) appears in the top `k` largest elements of the list. It prints 'YES' if all occurrences of `favorite_value` are in the top `k` elements, 'NO' if none of the `favorite_value` is in the top `k` elements, and 'MAYBE' otherwise.

