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
        
    #State: `t` is 0, `n`, `f`, `k` are integers provided by the input in the last iteration, `a` is the list of integers derived from the input in the last iteration where each integer `a_i` satisfies 1 <= `a_i` <= 100, `favorite_value` is `a[f - 1]` based on the last `a`, `sorted_a` is a sorted list of integers derived from the last `a` in descending order, `removed_count` is the number of times `favorite_value` appears in the first `k` elements of the last `sorted_a`, and `favorite_count` is the number of times `favorite_value` appears in the last `sorted_a`. The loop has finished executing all `t` iterations.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives integers `n`, `f`, and `k`, and a list `a` of `n` integers. It determines the `f`-th element in the list as the favorite value and checks how many times this favorite value appears in the top `k` largest elements of the list. It then prints 'YES' if all occurrences of the favorite value are within the top `k` largest elements, 'NO' if none of the occurrences are within the top `k`, and 'MAYBE' otherwise.

