#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n, f, and k are integers for each test case where 1 <= f, k <= n <= 100, and a is a list of n integers such that 1 <= a_i <= 100.
def func():
    for _ in range(int(input())):
        n, f, k = map(int, input().split())
        
        f -= 1
        
        k -= 1
        
        a = list(map(int, input().split()))
        
        x = a[f]
        
        a.sort(reverse=True)
        
        if a[k] > x:
            print('NO')
        elif a[k] < x:
            print('YES')
        else:
            print('YES' if k == n - 1 or a[k - 1] < x else 'MAYBE')
        
    #State: The loop iterates t times, and for each iteration, the values of n, f, k, and a are updated based on the input. After each iteration, the list a is sorted in descending order, and the output is either 'YES', 'NO', or 'MAYBE' depending on the conditions specified in the loop. The final state of the variables n, f, k, and a will be the values from the last test case after the loop completes all t iterations. The variable t will be 0, as the loop has completed all its iterations.
#Overall this is what the function does:The function processes `t` test cases, where each test case is defined by integers `n`, `f`, and `k`, and a list `a` of `n` integers. For each test case, it determines whether the `f`-th element in the original list `a` is greater than, less than, or equal to the `k`-th element in the sorted list `a` (in descending order). The function prints 'YES' if the `f`-th element is greater than the `k`-th element in the sorted list, 'NO' if it is less, and 'MAYBE' if they are equal but the `k`-th element is not the last element in the sorted list or if the element before it is less than the `f`-th element. After processing all `t` test cases, the final state of the variables `n`, `f`, `k`, and `a` will be the values from the last test case, and the variable `t` will be 0.

