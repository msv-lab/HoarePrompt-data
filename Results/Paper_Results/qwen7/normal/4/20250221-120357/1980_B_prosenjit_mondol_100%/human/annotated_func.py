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
            print('YES' if k == n - 1 or a[k + 1] < x else 'MAYBE')
        
    #State: t
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads three integers \( n \), \( f \), and \( k \) and a list of \( n \) integers \( a \). It then compares the \( f \)-th element of the sorted list (in descending order) with the \( k \)-th element. If the \( k \)-th element is greater than the \( f \)-th element, it prints 'NO'. If the \( k \)-th element is less than the \( f \)-th element, it prints 'YES'. If the \( k \)-th element is equal to the \( f \)-th element, it prints 'YES' if \( k \) is the last index or the element at \( k+1 \) is less than the \( f \)-th element; otherwise, it prints 'MAYBE'. The function does not return any value but prints the result for each test case.

