#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three positive integers n, a, and b such that 1 ≤ n, a, b ≤ 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print(b * k - k * (k - 1) // 2 + (n - k) * a)
        
    #State: Output State: The loop will continue to execute until all input test cases are processed. After all iterations, `n`, `a`, and `b` will hold the values provided by the last input test case, and `k` will be the minimum value between the final `n` and `b - a`. If `b` is less than or equal to `a` at the last iteration, `k` will be the minimum value between the final `n` and `b - a`. Otherwise, `k` will also be the minimum value between the final `n` and `b - a`. The output of each iteration is determined based on the current values of `n`, `a`, and `b`, and `k` is recalculated for each new set of inputs.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three positive integers \( n \), \( a \), and \( b \). It calculates and prints the result based on the values of \( n \), \( a \), and \( b \) for each test case. Specifically, it finds the minimum value between \( n \) and \( b - a \) and uses it to compute and print either \( a \times n \) or \( b \times k - k \times (k - 1) / 2 + (n - k) \times a \), depending on whether \( b \) is less than or equal to \( a \) or not. After processing all test cases, the function concludes with the final values of \( n \), \( a \), and \( b \) corresponding to the last input test case, and \( k \) being the minimum value between the final \( n \) and \( b - a \).

