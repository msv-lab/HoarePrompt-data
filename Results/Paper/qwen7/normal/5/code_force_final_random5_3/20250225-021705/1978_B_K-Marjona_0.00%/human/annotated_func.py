#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and each test case consists of three positive integers n, a, and b such that 1 ≤ n, a, b ≤ 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: All test cases have been processed, and the variable `t` is now 0. The variables `n`, `a`, and `b` are reset to their initial values for each test case, and `k` is recalculated based on the input for each test case.
#Overall this is what the function does:The function processes a specified number of test cases, where each test case consists of three positive integers \( n \), \( a \), and \( b \). For each test case, it calculates and prints one of two possible outputs based on the values of \( n \), \( a \), and \( b \). If \( b \leq a \), it prints \( a \times n \). Otherwise, it calculates and prints a specific formula involving \( b \), \( k \) (the minimum of \( n \) and \( b - a \)), and \( a \). After processing all test cases, the function ends with all input variables reset for each test case.

