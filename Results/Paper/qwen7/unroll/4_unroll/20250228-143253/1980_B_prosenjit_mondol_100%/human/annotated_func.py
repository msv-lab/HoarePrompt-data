#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100. a is a list of n integers such that 1 <= a_i <= 100 for all i.
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
        
    #State: Output State: The output state consists of a series of 'YES', 'NO', and 'MAYBE' based on the conditions evaluated for each test case within the loop. For each test case, the program compares the k-th largest element in the sorted list `a` with the element at index `f`. If the k-th largest element is greater than the element at index `f`, it prints 'NO'. If the k-th largest element is less than the element at index `f`, it prints 'YES'. If they are equal, it checks if the k-th element is the last element in the list; if so, it prints 'YES'; otherwise, it prints 'MAYBE'. This process repeats for each test case provided by the input.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads three integers \( n \), \( f \), and \( k \) along with a list of \( n \) integers \( a \). It then sorts the list \( a \) in descending order. The function compares the \( k \)-th largest element in the sorted list with the element at index \( f \). Based on the comparison, it prints either 'YES', 'NO', or 'MAYBE' for each test case. If the \( k \)-th largest element is greater than the element at index \( f \), it prints 'NO'. If the \( k \)-th largest element is less than the element at index \( f \), it prints 'YES'. If they are equal, it checks if the \( k \)-th element is the last element in the list; if so, it prints 'YES'; otherwise, it prints 'MAYBE'.

