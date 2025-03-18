#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and each test case consists of three positive integers n, a, and b such that 1 ≤ n, a, b ≤ 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print(b * k - k * (k - 1) // 2 + (n - k) * a)
        
    #State: Output State: The output state will consist of a series of lines, each containing the result of one test case's computation. For each test case, if \( b \leq a \), the output will be \( a \times n \). Otherwise, the output will be \( b \times k - \frac{k \times (k - 1)}{2} + (n - k) \times a \), where \( k = \min(n, b - a) \).
    #
    #This means for each test case, the output will either be a simple multiplication of \( a \) and \( n \) or a more complex expression involving \( b \), \( a \), and \( n \), depending on the values of \( a \), \( b \), and \( n \).
#Overall this is what the function does:The function processes a specified number of test cases, where each test case includes three positive integers \( n \), \( a \), and \( b \). For each test case, it calculates and prints a result based on the values of \( n \), \( a \), and \( b \). If \( b \leq a \), the result is \( a \times n \). Otherwise, the result is \( b \times k - \frac{k \times (k - 1)}{2} + (n - k) \times a \), where \( k = \min(n, b - a) \). After processing all test cases, it outputs the results for each case.

