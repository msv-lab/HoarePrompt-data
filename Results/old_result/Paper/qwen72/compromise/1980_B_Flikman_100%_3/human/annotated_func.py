#State of the program right berfore the function call: t is an integer such that 1 \le t \le 1000, n is an integer such that 1 \le n \le 100, f and k are integers such that 1 \le f, k \le n, and a is a list of n integers where 1 \le a_i \le 100.
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
        
    #State: `t` is 0, `_` is `t - 1`, `n`, `f`, and `k` are integers provided by the user, `a` is a list of integers provided by the user, `favorite_value` is the integer at index `f - 1` in the list `a`, `sorted_a` is a new list containing the elements of `a` sorted in descending order, `i` is `k - 1`, `k` is the number of iterations the loop will run, `favorite_count` is the total number of times `favorite_value` appears in `sorted_a`, and `removed_count` is the number of times `favorite_value` appears in the first `k` elements of `sorted_a`. If `removed_count` is equal to `favorite_count`, the program has printed 'YES' for all iterations. If `removed_count` is 0, the program has printed 'NO' for all iterations. Otherwise, the program has printed 'MAYBE' for all iterations.
#Overall this is what the function does:The function processes a series of test cases, each defined by integers `n`, `f`, and `k`, and a list `a` of `n` integers. For each test case, it determines if all occurrences of the value at index `f-1` in `a` are among the first `k` elements of `a` when sorted in descending order. If so, it prints 'YES'; if none of the occurrences are in the first `k` elements, it prints 'NO'; otherwise, it prints 'MAYBE'. After processing all `t` test cases, the function concludes with `t` being 0.

