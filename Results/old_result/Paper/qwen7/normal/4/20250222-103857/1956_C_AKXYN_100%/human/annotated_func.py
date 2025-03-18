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
        
    #State: Output State: `res` is 140, `t` is an integer such that \(1 \leq t \leq 500\), `n` is 1, `i` is 0, `mat` is a list of lists where each sublist contains integers from 1 to 1.
    #
    #Explanation: After analyzing the provided output states, we can infer the behavior of the loop. The variable `res` is calculated based on the formula \((i + 1) * (2 * i + 1)\) and summed up for each iteration. The variable `n` decreases with each iteration until it reaches 1. Once `n` is 1, the loop terminates because the inner loop runs from `n` down to 1, and when `i` becomes 0, the condition `i > 0` fails, stopping the loop.
    #
    #Given the output state after 3 iterations, we know that `n` was 6 initially and decreased to 1 after 3 iterations. Since the loop processes each `n` independently and `n` is reduced to 1 after 3 iterations, the final state will be when `n` is 1, and `i` is 0. At this point, `res` will be the cumulative sum calculated during the last iteration when `n` was 6, which is 140. The matrix `mat` will be a single list containing integers from 1 to 1, as `n` is now 1. The variable `t` remains unchanged as it is not affected by the loop.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of an integer `n`. For each `n`, it calculates a value `res` using the formula `(i + 1) * (2 * i + 1)` summed over all rows of a matrix `mat` of size `n x n`. It then prints `res` and `2 * n`. Following this, it prints two sequences of numbers from 1 to `n` for each row in reverse order. After processing all test cases, the function does not return any value but prints the results for each test case.

