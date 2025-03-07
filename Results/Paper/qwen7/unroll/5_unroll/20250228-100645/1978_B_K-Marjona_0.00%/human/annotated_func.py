#State of the program right berfore the function call: t is a positive integer indicating the number of test cases. For each test case, n, a, and b are positive integers such that 1 ≤ n, a, b ≤ 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: Output State: The output state consists of multiple lines, each corresponding to one test case. For each test case, if \( b \leq a \), the output is \( a \times n \). Otherwise, the output is \(\frac{(b + (b - k + 1))}{2} \times k + (n - k) \times a\), where \( k = \min(n, b - a) \).
    #
    #This means for each test case, the output will either be the product of \( a \) and \( n \) if \( b \) is less than or equal to \( a \), or a more complex calculation involving \( a \), \( b \), and \( n \) otherwise.
#Overall this is what the function does:The function processes a specified number of test cases (`t`). For each test case, it reads three positive integers (`n`, `a`, and `b`) and calculates and prints the result based on the following conditions: if `b` is less than or equal to `a`, it prints `a * n`; otherwise, it calculates and prints a value derived from `a`, `b`, and `n` using the formula \(\frac{(b + (b - k + 1))}{2} \times k + (n - k) \times a\), where \( k = \min(n, b - a) \). The function does not return any value but outputs the results for each test case.

