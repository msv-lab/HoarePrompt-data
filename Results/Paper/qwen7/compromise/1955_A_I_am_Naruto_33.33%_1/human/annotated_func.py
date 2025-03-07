#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n > 1:
            ans1 = a * n
            ans2 = b * n // 2 + a * n % 2
            print(min(ans1, ans2))
        else:
            print(a)
        
    #State: Output State: The output state consists of a series of minimum values printed for each test case. For each test case, if \( n > 1 \), the output is the minimum value between \( a \times n \) and \( b \times n // 2 + a \times n \% 2 \). If \( n = 1 \), the output is simply \( a \).
#Overall this is what the function does:The function processes up to 10,000 test cases, each consisting of three integers \( n \), \( a \), and \( b \). For each test case, it calculates either \( a \times n \) or \( b \times n // 2 + a \times n \% 2 \), depending on whether \( n \) is greater than 1. It then prints the minimum of these two values. If \( n = 1 \), it simply prints \( a \). After processing all test cases, the function concludes without returning any value.

