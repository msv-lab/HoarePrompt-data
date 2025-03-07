#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 1 ≤ n ≤ 500. Additionally, the sum of n^2 over all test cases does not exceed 5 × 10^5.
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
        
    #State: Output State: After the loop executes all its iterations, `j` will be `n + r + 1`, `n` will be the input integer, and `r` will remain non-negative and unchanged. The variable `sum` will contain the sum calculated during the loop's execution, and `t` will be 0 since all test cases have been processed. The loop will have printed sequences for each value of `j` from 1 to `n + r + 1`, following the specified rules for printing based on whether `j` is less than or equal to `n` or greater than `n`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `t` (number of test cases) and an integer `n` (an integer within the range 1 to 500). For each test case, it calculates a sum based on specific conditions and prints the sum along with another integer `r`. It then prints sequences of numbers based on the value of `j` ranging from 1 to `n + r + 1`. After processing all test cases, the function outputs the final state where `t` is set to 0, indicating all test cases have been processed.

