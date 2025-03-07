#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 2 ≤ n ≤ 10^3.
def func():
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: Output State: `i` will be `n + 1`, and `n` must be greater than 5.
    #
    #Explanation: After the loop has executed all its iterations, the final value of `i` will be `n + 1`. The loop starts with `i` as 3 and increments `i` by 1 in each iteration until it reaches `n`. For the loop to run all iterations, `n` must be greater than 5, as it needs to go through at least 3 increments (from 3 to 4, then 4 to 5, and so on) to reach `n`. Therefore, after the loop completes, `i` will be `n + 1` and `n` must be greater than 5.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of two integers \( t \) and \( n \). For each test case, if \( 1 \leq t \leq 50 \) and \( 2 \leq n \leq 10^3 \), it prints specific pairs of integers. Specifically, it prints "1 1", "1 2", followed by pairs "i i" for \( i \) ranging from 3 to \( n \). After processing all test cases, the function does not return any value.

