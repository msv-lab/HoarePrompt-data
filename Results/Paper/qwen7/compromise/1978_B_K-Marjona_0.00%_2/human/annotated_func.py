#State of the program right berfore the function call: t is a positive integer indicating the number of test cases. For each test case, n, a, and b are positive integers such that 1 \le n, a, b \le 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: Output State: The output state will consist of multiple lines, each corresponding to the result of one test case. For each test case, if \( b > a \), the output will be the sum of an arithmetic sequence starting from \( b \) with a common difference of 1, truncated to the first \( k \) terms, plus the product of \( a \) and the remaining terms. If \( b \leq a \), the output will simply be \( a \times n \). Here, \( k \) is the minimum value between \( n \) and \( b - a \).
    #
    #This output state describes the results of processing each test case according to the given loop logic.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three positive integers \( n \), \( a \), and \( b \) (where \( 1 \le n, a, b \le 10^9 \)). For each test case, it calculates and prints the sum of an arithmetic sequence or a simple product based on the values of \( a \) and \( b \). Specifically, if \( b > a \), it computes the sum of the first \( k \) terms of an arithmetic sequence starting from \( b \) with a common difference of 1, plus the product of \( a \) and the remaining terms, where \( k \) is the minimum value between \( n \) and \( b - a \). If \( b \le a \), it simply prints \( a \times n \). The function outputs the results for all test cases.

