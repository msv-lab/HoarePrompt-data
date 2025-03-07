#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 1 ≤ n ≤ 500. Additionally, the sum of n^2 over all test cases does not exceed 5 × 10^5.
def func_1():
    n = int(input())
    print(n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    #This is printed: k * (k + 1) * (4 * k - 1) // 6, 2 * k
    for i in range(1, n + 1):
        print(1, i, *range(n, 0, -1))
        
        print(2, i, *range(n, 0, -1))
        
    #State: Output State: The loop will execute `n` times, with `i` ranging from 1 to `n`. After all iterations, `i` will be equal to `n`, and `n` can be any integer between 1 and 500, inclusive.
    #
    #This means that after the loop completes all its iterations, the final value of `i` will be the same as the final value of `n`, and `n` will be the maximum value it was initialized to or updated to during the loop's execution, which is constrained to be between 1 and 500.
#Overall this is what the function does:The function processes a series of test cases, where each test case involves an integer `n` (1 ≤ n ≤ 500). For each test case, it calculates and prints the value of \( \frac{n(n+1)(4n-1)}{6} \) and 2n. It then prints two lines for each value of `i` from 1 to `n`, each containing `i`, `i`, and a sequence of numbers from `n` down to 1. After processing all test cases, the function does not return any value but prints the results for each test case.

