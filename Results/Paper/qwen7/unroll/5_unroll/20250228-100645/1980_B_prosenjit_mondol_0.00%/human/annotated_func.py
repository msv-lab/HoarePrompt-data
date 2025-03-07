#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100. a is a list of n integers such that 1 <= a_i <= 100 for all 1 <= i <= n.
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
        
    #State: Output State: t test cases have been processed. For each test case, either 'NO', 'YES', or 'MAYBE' has been printed based on the conditions given in the loop. The values of n, f, k, a, and x have been updated according to the loop's logic, but their specific values are not preserved outside of each test case iteration.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads integers `n`, `f`, and `k`, and a list `a` of `n` integers. It then sorts the list `a` in descending order. Based on the comparison between the `f`-th element and the `k`-th element of the sorted list, it prints either 'NO', 'YES', or 'MAYBE'. After processing all test cases, the function does not return any value but prints the results for each test case.

