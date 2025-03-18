#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000. For each test case, n, f, and k are positive integers such that 1 <= f, k <= n <= 100. a is a list of n integers where 1 <= a_i <= 100 for each a_i in a.
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
        
    #State: Output State: The output state consists of a series of 'YES', 'NO', and 'MAYBE' based on the comparison between the k-th largest element and the f-th element in the sorted list of integers a for each test case. Each test case is processed independently, and the output for each test case is printed on a new line.
#Overall this is what the function does:The function processes multiple test cases, each defined by positive integers \( t \), \( n \), \( f \), \( k \), and a list of \( n \) integers \( a \). For each test case, it sorts the list \( a \) in descending order and compares the \( k \)-th largest element with the \( f \)-th element. Based on the comparison, it prints either 'YES', 'NO', or 'MAYBE'. The function does not return any value but prints the result for each test case.

