#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 1 ≤ n ≤ 500. Additionally, the sum of n² over all test cases does not exceed 5 × 10⁵.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        sum, r = 0, 0
        
        for i in range(1, n + 1):
            if n * (n + 1) // 2 > i * n:
                r = i
                sum += n * (n + 1) // 2
            else:
                sum += i * n
        
        print(sum, n + r)
        
        for j in range(1, n + r + 1):
            if j <= n:
                print(1, j, end=' ')
                print(*range(1, n + 1))
            else:
                print(2, j % n, end=' ')
                print(*range(1, n + 1))
        
    #State: Output State: j = 3 * n + 3, n = initial n, r = 3, sum = 3 * n * n + n * (n + 1) // 2.
    #
    #After the loop executes all its iterations, the value of `j` will be `3 * n + 3`, as it increments by `1` in each iteration of the loop. The value of `n` remains unchanged throughout the loop iterations. The value of `r` is set to `3` after the third iteration. The value of `sum` is calculated as `3 * n * n + n * (n + 1) // 2`, which represents the sum accumulated over all three iterations of the loop.
#Overall this is what the function does:The function processes multiple test cases, each involving two integers \( t \) and \( n \). For each test case, it calculates a sum based on specific conditions and prints the sum along with certain values. It also prints a sequence of numbers in a particular format. After processing all test cases, the function outputs the final state of the variables \( j \), \( n \), and \( r \) as described in the annotation.

