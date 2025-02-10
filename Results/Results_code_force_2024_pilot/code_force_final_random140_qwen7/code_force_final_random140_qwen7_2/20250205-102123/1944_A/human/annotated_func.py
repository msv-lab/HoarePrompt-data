#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, each test case consists of two integers n and k such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ (n * (n - 1)) / 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k > 1 else 1)
        
    #State: Output State: The loop will have processed all input test cases. For each test case, `n` is the first integer input, `k` is the second integer input, and the output will be `n` if `n - k > 1`, otherwise `1`. There is no specific value given for the final `new_input` as it is not defined in the provided loop, but it implies that after processing all inputs, there would be no further input to process.
    #
    #In simpler terms, after all iterations of the loop, we will have processed all test cases. For each case, if `n - k` is greater than 1, the output will be `n`; otherwise, the output will be `1`. There are no further inputs to process after the loop completes.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( n \) and \( k \). For each test case, it checks if \( n - k > 1 \). If true, it outputs \( n \); otherwise, it outputs 1. After processing all test cases, the function concludes with no further inputs to process.

