#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000. For each test case, n, f, and k are positive integers such that 1 <= f, k <= n <= 100. a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 100.
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
        
    #State: Output State: The output state consists of a series of 'NO', 'YES', and 'MAYBE' based on the comparison between the k-th largest element and the f-th element in the sorted list a for each test case. For each test case, if the k-th largest element is greater than the f-th element, the output is 'NO'. If the k-th largest element is less than the f-th element, the output is 'YES'. If they are equal, the output is 'YES' unless the k-th element is the second largest element in the list (i.e., k is the last index), in which case the output is 'MAYBE'.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads three integers \( n \), \( f \), and \( k \) along with a list of \( n \) integers \( a \). It then sorts the list \( a \) in descending order. After sorting, it compares the \( k \)-th largest element with the \( f \)-th element. If the \( k \)-th largest element is greater than the \( f \)-th element, it prints 'NO'. If the \( k \)-th largest element is less than the \( f \)-th element, it prints 'YES'. If they are equal, it prints 'YES' unless the \( k \)-th element is the second largest element in the list, in which case it prints 'MAYBE'.

