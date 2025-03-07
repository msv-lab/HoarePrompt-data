#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are positive integers such that 1 ≤ n, a, b ≤ 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: Output State: The output state consists of a series of integers printed for each test case. For each test case, if \( b \leq a \), the output is \( a \times n \). Otherwise, the output is \(\frac{(b + (b - k + 1))}{2} \times k + (n - k) \times a\), where \( k = \min(n, b - a) \).
    #
    #This means for each test case, the program calculates and prints either \( a \times n \) or a more complex expression based on the values of \( n \), \( a \), and \( b \), depending on whether \( b \) is less than or equal to \( a \).
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers \( t \), \( n \), and \( a \). For each test case, it calculates and prints either \( a \times n \) or a more complex expression based on the values of \( n \) and \( a \), depending on whether \( b \) (which is not explicitly passed but derived from the input) is less than or equal to \( a \). If \( b \leq a \), it prints \( a \times n \); otherwise, it prints \(\frac{(b + (b - k + 1))}{2} \times k + (n - k) \times a\), where \( k = \min(n, b - a) \). The function does not return any value but outputs the results for each test case.

