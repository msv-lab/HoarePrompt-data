#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 1 ≤ n ≤ 500. Additionally, the sum of n^2 over all test cases does not exceed 5 × 10^5.
def func_1():
    n = int(input())
    print(n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    #This is printed: n * (n + 1) * (4 * n - 1) // 6, 2 * n
    for i in range(1, n + 1):
        print(1, i, *range(n, 0, -1))
        
        print(2, i, *range(n, 0, -1))
        
    #State: Output State: `t` is an integer such that \(1 \leq t \leq 500\), `i` is equal to `n`, `n` must be at least 3.
    #
    #Explanation: After the loop has executed all its iterations, the variable `i` will be equal to the final value of `n` because the loop runs from `1` to `n`. The initial value of `t` remains unchanged as it is not affected by the loop. The variable `n` must be at least 3 since the loop was able to execute 3 times, meaning `n` was initially at least 3 or more.
#Overall this is what the function does:The function processes a series of test cases, each defined by integers `t` and `n` (where `1 ≤ t ≤ 500` and `1 ≤ n ≤ 500`), and calculates and prints a mathematical expression `n * (n + 1) * (4 * n - 1) // 6` along with `2 * n`. It then prints two sequences of numbers for each `n` from 1 to `n`, each sequence being a range from `n` down to 1. After processing, the function ensures that `n` is at least 3 and `t` remains unchanged.

