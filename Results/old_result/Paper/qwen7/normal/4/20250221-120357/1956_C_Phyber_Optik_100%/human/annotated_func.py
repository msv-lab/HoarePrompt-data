#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 1 ≤ n ≤ 500. Additionally, the sum of n^2 over all test cases does not exceed 5 × 10^5.
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
        
    #State: Output State: The loop will run `t` times, where `t` is the input integer. For each iteration, `j` will range from 1 to `n`, and the loop will print two lines for each value of `j`. After all iterations, `j` will be `n + 1` for each of the `t` iterations, `i` will be `n + 1` since it is incremented up to `n` in the inner loop but not reset, and `sum` will be the sum calculated for the last value of `n`. The variable `n` will remain the same as the input for each iteration.
    #
    #In natural language, the output state after the loop executes all its iterations is: The loop will run `t` times, with `j` ranging from 1 to `n` for each iteration. After all iterations, `j` will be `n + 1`, `i` will be `n + 1`, `sum` will be the final sum calculated for the last value of `n`, and `n` will be the original input integer.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \( t \) and \( n \). It calculates a sum based on the formula provided and prints the sum along with \( 2n \). Additionally, it prints two lines for each value of \( j \) ranging from 1 to \( n \), where \( j \) is the loop variable. After processing all test cases, the function does not return any value but outputs the results for each test case.

