#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000. For each test case, n, f, and k are positive integers such that 1 <= f, k <= n <= 100. a is a list of n integers such that 1 <= a_i <= 100 for all 1 <= i <= n.
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
        
    #State: Output State: The output state consists of a series of 'NO', 'YES', and 'MAYBE' based on the comparison between the k-th largest element in the sorted list `a` (after sorting in descending order) and the element at index `f` in the original list `a`. If the k-th largest element is greater than the element at index `f`, the output is 'NO'. If it is smaller, the output is 'YES'. If they are equal, the output is 'YES' unless the k-th element is the last element in the list and the (k+1)-th element is not smaller than the element at index `f`, in which case the output is 'MAYBE'.
#Overall this is what the function does:The function processes multiple test cases, each defined by positive integers \( n \), \( f \), and \( k \), and a list \( a \) of \( n \) integers. For each test case, it sorts the list \( a \) in descending order and compares the element at index \( f \) with the \( k \)-th largest element in the sorted list. Based on this comparison, it prints 'NO', 'YES', or 'MAYBE' for each test case.

