#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 1 ≤ n ≤ 500. Additionally, the sum of n² over all test cases does not exceed 5 × 10⁵.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        sum = 1
        
        for i in range(2, n + 1):
            sum += (i * i - (i - 1) * (i - 1)) * i
        
        print(sum, n + n)
        
        for j in range(1, n + 1):
            print(1, n - j + 1, *range(1, n + 1))
            print(2, n - j + 1, *range(1, n + 1))
        
    #State: Output State: The loop has executed all its iterations, and the final state of the variables is as follows: `sum` is 156, `i` is 3, `j` is 6, `n` is at least 6, and `t` is greater than 0. The loop has completed its execution, and the values of `sum`, `i`, `j`, `n`, and `t` reflect the state after all iterations.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \( t \) and \( n \), where \( 1 \leq t \leq 500 \) and \( 1 \leq n \leq 500 \). For each test case, it calculates a sum based on a specific formula involving squares of integers and prints the sum along with another value derived from \( n \). It then prints multiple lines of output, each containing specific sequences of numbers based on \( n \). After processing all test cases, the function concludes with no return value.

