#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 100.
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
        
    #State: `t` is 0; `n`, `f`, `k`, and `a` hold the values from the last iteration; `favorite_value` is `a[f - 1]` from the last iteration; `sorted_a` is the list `a` sorted in descending order from the last iteration; `removed_count` is the number of times `favorite_value` appears in the first `k` elements of `sorted_a` from the last iteration; `favorite_count` is the number of times `favorite_value` appears in the entire `sorted_a` list from the last iteration.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `f`, `k`, and a list `a` of `n` integers. For each test case, it determines if the favorite value (the value at index `f-1` in list `a`) can be removed from the top `k` largest values in `a`. It prints 'YES' if all occurrences of the favorite value within the top `k` largest values are removed, 'NO' if none are removed, and 'MAYBE' otherwise.

