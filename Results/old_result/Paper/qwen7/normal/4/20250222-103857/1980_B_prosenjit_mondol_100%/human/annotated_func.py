#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000. For each test case, n, f, and k are positive integers such that 1 <= f, k <= n <= 100. a is a list of n integers such that 1 <= a_i <= 100 for all i in range(n).
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
            print('YES' if k == n - 1 or a[k + 1] < x else 'MAYBE')
        
    #State: After all iterations of the loop have finished, `t` remains a positive integer such that \(1 \leq t \leq 1000\). For each test case, `n` is the last integer input, `f` is the last integer input decreased by the total number of iterations minus one, `k` is also the last integer input decreased by the total number of iterations minus one. The list `a` is a list of `n` integers sorted in descending order, with `x` being the element at index `f` in list `a`. If `a[k] > x`, the output will be 'NO'. Otherwise, the output will be 'YES' or 'MAYBE' based on the conditions provided in the loop body.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads three integers \(n\), \(f\), and \(k\) along with a list \(a\) of \(n\) integers. It then sorts the list \(a\) in descending order. Based on the values of \(a[k]\) and \(a[f]\), it prints either 'NO', 'YES', or 'MAYBE'. The function does not return any value but prints the result for each test case.

