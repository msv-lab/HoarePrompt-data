#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and each test case consists of three positive integers n, a, and b such that 1 ≤ n, a, b ≤ 10^9.
def func():
    t = int(input())
    while t:
        x = list(map(int, input().split(' ')))
        
        n = x[0]
        
        a = x[1]
        
        b = x[2]
        
        profit = n * a
        
        if a >= b:
            print(profit)
        else:
            k = b - a
            k = min(n - 1, k)
            profit = profit + (b - a) * (k + 1) - k * (k + 1) / 2
            print(int(profit))
        
        t -= 1
        
    #State: Output State: `t` is equal to 0, and the output consists of the final profit value calculated for each test case after the loop has executed all its iterations.
    #
    #In natural language: After the loop has completed all its iterations, the variable `t` will be 0 because it is decremented by 1 in each iteration until it reaches 0. The output will consist of the final profit values for each of the test cases processed, printed during each iteration of the loop based on the conditions specified within the loop body.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of three positive integers `n`, `a`, and `b`. For each test case, it calculates a profit value based on the given conditions. If `a` is greater than or equal to `b`, it prints the initial profit value `n * a`. Otherwise, it calculates a modified profit value using the formula `profit + (b - a) * (k + 1) - k * (k + 1) / 2` where `k` is the minimum of `b - a` and `n - 1`. After processing all test cases, it outputs the final profit values for each test case.

