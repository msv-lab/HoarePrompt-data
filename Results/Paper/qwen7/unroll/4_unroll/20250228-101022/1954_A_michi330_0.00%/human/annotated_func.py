#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n, m, and k are positive integers satisfying 1 ≤ m, k ≤ n ≤ 50.
def func():
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) < k:
            print('NO')
        else:
            print('Yes')
        
    #State: The output state will consist of 'YES' or 'NO' printed for each test case based on the conditions given in the loop. The number of 'YES' and 'NO' printed will depend on the input values provided for each test case (n, m, k).
#Overall this is what the function does:The function reads multiple test cases, each consisting of three positive integers \( n \), \( m \), and \( k \). For each test case, it checks if \( n \leq k \) or if \( n - \lceil \frac{n}{m} \rceil < k \). If either condition is true, it prints 'NO'; otherwise, it prints 'YES'. The function processes up to 1000 test cases.

