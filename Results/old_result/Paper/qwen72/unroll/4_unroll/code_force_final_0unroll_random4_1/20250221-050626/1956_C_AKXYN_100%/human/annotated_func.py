#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, and for each test case, n is an integer such that 1 <= n <= 500.
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
        
    #State: The loop has finished executing for all test cases. For each test case, the value of `res` is the sum of (i + 1) * (2 * i + 1) for i from 0 to n-1, and the value of `n << 1` is 2 * n. Additionally, for each test case, the loop prints two lines for each i from n to 1: the first line is "1 i" followed by the numbers from 1 to n, and the second line is "2 i" followed by the numbers from 1 to n. The initial state of `t` and `n` remains unchanged, but the loop has been executed for each test case.
#Overall this is what the function does:The function processes a series of test cases, where the number of test cases `t` is an integer between 1 and 500. For each test case, it reads an integer `n` (1 <= n <= 500) from the input. It then calculates the sum of `(i + 1) * (2 * i + 1)` for `i` ranging from 0 to `n-1` and prints this sum along with `2 * n`. Additionally, for each `i` from `n` down to 1, it prints two lines: the first line is "1 i" followed by the numbers from 1 to `n`, and the second line is "2 i" followed by the numbers from 1 to `n`. The function does not return any value; it only prints the results to the console. After the function concludes, the initial state of `t` and `n` remains unchanged, but the specified output has been printed for each test case.

