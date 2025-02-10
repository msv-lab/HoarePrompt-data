#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        s1 = n * a
        
        s2 = b * (n // 2) + n % 2 * a
        
        print(min(s1, s2))
        
    #State: t is an integer such that \(1 \leq t \leq 10^4\), `n` is the final integer input, `a` is the second integer input, `b` is the third integer input, `s1` is `n * a`, `s2` is `b * (n // 2) + n % 2 * a`
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers \(n\), \(a\), and \(b\) (where \(1 \leq n \leq 100\) and \(1 \leq a, b \leq 30\)). For each test case, it calculates two values, \(s1 = n \times a\) and \(s2 = b \times (n // 2) + n \% 2 \times a\), and prints the minimum of these two values. After processing all test cases, the function does not return any value.

