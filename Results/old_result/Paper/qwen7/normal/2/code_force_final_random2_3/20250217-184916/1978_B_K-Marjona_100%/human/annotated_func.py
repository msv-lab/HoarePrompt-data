#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and each test case consists of three positive integers n, a, and b such that 1 ≤ n, a, b ≤ 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print(b * k - k * (k - 1) // 2 + (n - k) * a)
        
    #State: t is 0, and there are no further values of n, a, and b as the loop has completed all its iterations. k retains its last computed value for each test case.
#Overall this is what the function does:The function processes a specified number of test cases (determined by user input). For each test case, it reads three integers \( n \), \( a \), and \( b \). It then calculates and prints a result based on the relationship between \( a \) and \( b \). If \( b \leq a \), it prints \( a \times n \). Otherwise, it computes and prints \( b \times k - k \times (k - 1) / 2 + (n - k) \times a \), where \( k \) is the minimum of \( n \) and \( b - a \). After processing all test cases, the function does not return any value.

