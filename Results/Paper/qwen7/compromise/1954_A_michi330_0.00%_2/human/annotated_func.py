#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. Each test case consists of three positive integers n, m, and k such that 1 ≤ m, k ≤ n ≤ 50.
def func():
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) < k:
            print('NO')
        else:
            print('Yes')
        
    #State: The output state will consist of 'YES' or 'NO' printed for each test case based on the conditions given in the loop. Specifically, for each test case, if \( n \leq k \) or \( n - \lceil \frac{n}{m} \rceil < k \), 'NO' will be printed; otherwise, 'YES' will be printed. The number of lines with 'YES' or 'NO' will correspond to the value of \( t \).
#Overall this is what the function does:The function processes a series of test cases, each consisting of three positive integers \( n \), \( m \), and \( k \). For each test case, it checks if \( n \leq k \) or if \( n - \lceil \frac{n}{m} \rceil < k \). If either condition is true, it prints 'NO'; otherwise, it prints 'YES'. After processing all test cases, the function concludes with the output containing 'YES' or 'NO' for each test case.

