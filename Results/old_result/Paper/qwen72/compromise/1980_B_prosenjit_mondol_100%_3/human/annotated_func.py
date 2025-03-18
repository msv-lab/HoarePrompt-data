#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 100, f and k are integers such that 1 <= f, k <= n, and a is a list of n integers such that 1 <= a_i <= 100.
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
        
    #State: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 100, f and k are integers such that 1 <= f, k <= n, and a is a list of n integers such that 1 <= a_i <= 100. The loop has executed all iterations, and for each iteration, the list `a` has been sorted in descending order, and the values of `f` and `k` have been decremented by 1. The loop has printed 'NO', 'YES', or 'MAYBE' for each iteration based on the conditions described in the loop.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n`, and two indices `f` and `k` (both 1-based), followed by a list `a` of `n` integers. It then checks if the element at index `f` (0-based) in the original list is greater than, less than, or equal to the element at index `k` (0-based) in the sorted list (in descending order). If the element at `f` is greater than the element at `k` in the sorted list, it prints 'NO'. If it is less, it prints 'YES'. If they are equal, it prints 'YES' if `k` is the last index of the sorted list or the next element in the sorted list is less than the element at `f`, otherwise it prints 'MAYBE'. The function does not return any value.

