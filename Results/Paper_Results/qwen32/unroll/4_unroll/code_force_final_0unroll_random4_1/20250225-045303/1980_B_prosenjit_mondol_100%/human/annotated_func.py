#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100, and a is a list of n integers where each element a_i satisfies 1 <= a_i <= 100.
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
        
    #State: The output state consists of t lines, each corresponding to the result of the comparison for each test case. Each line will contain either 'YES', 'NO', or 'MAYBE' based on the conditions specified in the loop. The variables n, f, k, a, x are not preserved across iterations and revert to their initial state at the beginning of each test case. The variable t remains unchanged as it represents the number of test cases.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it receives integers `n`, `f`, and `k`, and a list `a` of `n` integers. It compares the `f`-th element of the list `a` with the `k`-th largest element in the list. It outputs 'YES' if the `f`-th element is less than the `k`-th largest element, 'NO' if it is greater, and 'MAYBE' if they are equal and the `k`-th largest element is not the last element in the sorted list or if the next element in the sorted list is less than the `f`-th element.

