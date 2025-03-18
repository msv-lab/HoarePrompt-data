#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n, f, and k are integers for each test case such that 1 <= f, k <= n <= 100, and a is a list of n integers such that 1 <= a_i <= 100.
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
        
    #State: The loop executes `t` times, and for each iteration, it reads `n`, `f`, and `k` from input, reads a list `a` of `n` integers from input, and then prints 'YES', 'NO', or 'MAYBE' based on the conditions provided. After all iterations, `t` is unchanged, and the values of `n`, `f`, `k`, and `a` from the last iteration are the final values of these variables.
#Overall this is what the function does:The function `func` reads an integer `t` representing the number of test cases. For each test case, it reads three integers `n`, `f`, and `k`, and a list `a` of `n` integers. It then checks if the `k` largest elements in the list `a` include all occurrences of the value at index `f-1` in `a`. If all occurrences are included, it prints 'YES'. If none of the occurrences are included, it prints 'NO'. If some but not all occurrences are included, it prints 'MAYBE'. After processing all test cases, the function does not return any value, but the final values of `n`, `f`, `k`, and `a` from the last test case remain in memory.

