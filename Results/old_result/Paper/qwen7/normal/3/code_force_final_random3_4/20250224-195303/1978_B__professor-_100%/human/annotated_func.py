#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three positive integers n, a, and b such that 1 ≤ n, a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if b <= a:
            print(n * a)
        elif b - a >= n:
            print(int((2 * b - n + 1) * n // 2))
        else:
            print(int((b - a) * (b - a + 1) // 2 + a * n))
        
    #State: t is 1, n is the first integer from the input, a is the second integer from the input, b is the third integer from the input.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three positive integers \( t \), \( n \), and \( a \). It reads \( t \) test cases from the input, where \( 1 \leq t \leq 10^4 \). For each test case, it reads \( n \), \( a \), and \( b \) (where \( 1 \leq n, a, b \leq 10^9 \)). Depending on the values of \( b \) relative to \( a \) and \( n \), it prints one of the following: \( n \times a \), \( \frac{(2b - n + 1) \times n}{2} \), or \( \frac{(b - a) \times (b - a + 1)}{2} + a \times n \). If \( t \) is out of the specified range, it does not process any test cases.

