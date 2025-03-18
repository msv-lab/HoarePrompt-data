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
        
    #State: Output State: The output state consists of a series of 'YES', 'NO', and 'MAYBE' based on the comparison between the k-th largest element and the f-th element in the sorted list of integers provided for each test case. For each test case, the values of `n`, `f`, `k`, and `a` are read from input, and the program checks if the k-th largest element in the sorted list is greater than, less than, or equal to the f-th element. If the k-th largest element is greater, it prints 'NO'. If it is less, it prints 'YES'. If they are equal, it prints 'YES' unless the k-th element is the second last element in the list and the next element (k+1) is also equal to the f-th element, in which case it prints 'MAYBE'. This process repeats for each test case provided in the input.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads three integers \( n \), \( f \), and \( k \), and a list of \( n \) integers \( a \). It then sorts the list \( a \) in descending order. The function compares the \( k \)-th largest element in the sorted list with the \( f \)-th element. If the \( k \)-th largest element is greater than the \( f \)-th element, it prints 'NO'. If the \( k \)-th largest element is less than the \( f \)-th element, it prints 'YES'. If the \( k \)-th and \( f \)-th elements are equal, it prints 'YES' unless the \( k \)-th element is the second last element in the list and the next element is also equal to the \( f \)-th element, in which case it prints 'MAYBE'. This process is repeated for each test case provided in the input.

