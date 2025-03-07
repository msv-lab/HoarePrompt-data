#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100. a is a list of n integers such that 1 <= a_i <= 100 for all i in range n.
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
        
    #State: After all iterations of the loop have finished, the variable `t` will be the total number of test cases, which is an integer between 1 and 1000. For each test case, `n` will be the number of elements in the list `a`, `f` will be the original `f` minus the number of times the loop has executed, `k` will be the original `k` minus the number of times the loop has executed, and `a` will be a list of integers sorted in descending order. The variable `x` will be the element at index `f` in the list `a`. The loop will print either 'NO', 'YES', or 'MAYBE' based on the comparison between `a[k]` and `x`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer list `a` of length `n`, two indices `f` and `k` (both initially within the bounds of `a`), and determines whether the element at index `f` in the sorted list `a` is greater than the element at index `k`. If the element at `f` is greater than the element at `k`, it prints 'NO'. If the element at `f` is less than the element at `k`, it prints 'YES'. If the elements are equal, it prints 'YES' unless the element at `k-1` is also equal to the element at `f`, in which case it prints 'MAYBE'. The function implicitly accepts the number of test cases `t` as input and iterates through them, printing the result for each test case.

