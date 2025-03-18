#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 1 ≤ n ≤ 500. Additionally, the sum of n^2 over all test cases does not exceed 5 × 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        mat = [list(range(1, n + 1)) for i in range(n)]
        
        res = 0
        
        for i in range(n):
            res += (i + 1) * (2 * i + 1)
        
        print(res, n << 1)
        
        for i in range(n, 0, -1):
            print('1 %d' % i, *range(1, n + 1))
            print('2 %d' % i, *range(1, n + 1))
        
    #State: Output State: t test cases are printed, each followed by two lines of output. For each test case:
    #1. A line with two numbers: the first number is the sum \( \sum_{i=0}^{n-1} (i+1)(2i+1) \), and the second number is \( 2n \).
    #2. n lines, each starting with '1 n', followed by the sequence from 1 to n.
    #3. n lines, each starting with '2 n', followed by the sequence from 1 to n.
    #
    #The value of \( n \) for each test case is determined by user input, and the process is repeated for each test case specified by the first input.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` (1 ≤ n ≤ 500). For each test case, it calculates the sum \( \sum_{i=0}^{n-1} (i+1)(2i+1) \) and prints this sum along with \( 2n \). It then prints `n` lines for each test case, each starting with '1 n' followed by the sequence from 1 to n, and another `n` lines starting with '2 n' followed by the same sequence.

