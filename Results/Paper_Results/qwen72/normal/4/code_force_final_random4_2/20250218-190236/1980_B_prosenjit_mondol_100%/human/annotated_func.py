#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100, and a is a list of n integers such that 1 <= a_i <= 100.
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
        
    #State: The loop has executed `t` times, where `t` is the integer provided initially. For each of the `t` test cases, `n` is the integer provided for that test case and must be greater than 0, `f` is the second integer provided for that test case minus 1, `k` is the third integer provided for that test case minus 1, `a` is a sorted list of integers in descending order, and `x` is the integer at index `f` of the sorted list `a`. If `a[k]` is greater than `x`, the output for that test case is 'NO'. If `a[k]` is less than `x`, the output for that test case is 'YES'. If `a[k]` is equal to `x`, the output for that test case is 'YES' if `k` is the last index of the list or the integer at index `k + 1` of the sorted list `a` is less than `x`, otherwise it is 'MAYBE'.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `f`, and `k`, and a list `a` of `n` integers. For each test case, it determines the relationship between the `f`-th element (0-indexed) of the original list and the `k`-th element (0-indexed) of the sorted list in descending order. The function prints 'NO' if the `k`-th element in the sorted list is greater than the `f`-th element in the original list, 'YES' if the `k`-th element is less than the `f`-th element, and 'MAYBE' if they are equal and the `k`-th element is not the last in the list or the next element is also equal to the `f`-th element. After processing all test cases, the function has no return value.

