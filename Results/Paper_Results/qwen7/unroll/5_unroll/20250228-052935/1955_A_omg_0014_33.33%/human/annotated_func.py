#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        d = c / 2
        
        if a * b < a * d:
            print(a * b)
        else:
            print(round(a * d))
        
    #State: Output State: The output state will consist of `n` lines, each containing either the value of `a * b` or `round(a * d)`, depending on whether `a * b` is less than `a * d` or not for each iteration of the loop. The values of `a`, `b`, and `c` are read from the input for each iteration, and `d` is calculated as `c / 2`. The comparison between `a * b` and `a * d` determines which value is printed.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \( n \), \( a \), and \( b \). For each test case, it calculates \( d \) as half of \( c \) (where \( c \) is read alongside \( a \) and \( b \)), then compares \( a \times b \) with \( a \times d \). If \( a \times b \) is less than \( a \times d \), it prints \( a \times b \); otherwise, it prints the rounded value of \( a \times d \). After processing all test cases, it outputs \( n \) lines, each containing one of the computed values.

