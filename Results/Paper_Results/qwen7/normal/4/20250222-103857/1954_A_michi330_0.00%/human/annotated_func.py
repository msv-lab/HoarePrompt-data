#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n, m, and k are positive integers satisfying 1 ≤ m, k ≤ n ≤ 50.
def func():
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) < k:
            print('NO')
        else:
            print('Yes')
        
    #State: t is an integer between 1 and 1000 inclusive; n, m, and k are integers assigned the values from the input split for each iteration; itest equals t after all iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers \( n \), \( m \), and \( k \) (with constraints \( 1 \leq m, k \leq n \leq 50 \)). For each test case, it checks if \( n \) is greater than or equal to \( k \) and if \( n \) minus the ceiling of \( n \) divided by \( m \) is also greater than or equal to \( k \). If either condition fails, it prints 'NO'. Otherwise, it prints 'Yes'. After processing all test cases, it returns nothing explicitly but modifies the output stream by printing 'Yes' or 'No' for each test case.

