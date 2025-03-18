#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 100, f and k are integers such that 1 <= f, k <= n, and a is a list of n integers such that 1 <= a_i <= 100.
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
        
    #State: t is an input integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 100, f and k are integers such that 1 <= f, k <= n, and a is a list of n integers such that 1 <= a_i <= 100. The loop has executed all iterations, and the values of n, f, k, and a are reset for each iteration, so they do not retain any specific values from the previous iterations. The loop prints 'YES', 'NO', or 'MAYBE' for each iteration based on the conditions specified in the loop.
#Overall this is what the function does:The function `func` reads an integer `t` from user input, indicating the number of test cases. For each test case, it reads three integers `n`, `f`, and `k`, and a list `a` of `n` integers. It then determines the presence of the value at index `f-1` in the top `k` largest values of the list `a`. If all occurrences of this value are among the top `k` largest values, it prints 'YES'. If none of the occurrences are among the top `k` largest values, it prints 'NO'. If some but not all occurrences are among the top `k` largest values, it prints 'MAYBE'. The function does not return any value.

