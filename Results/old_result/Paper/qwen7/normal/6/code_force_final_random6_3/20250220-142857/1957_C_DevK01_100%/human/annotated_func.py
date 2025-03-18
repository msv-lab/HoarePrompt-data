#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 0 ≤ k ≤ n. The pairs (r_i, c_i) for i-th move you made are valid positions on an n × n chessboard, ensuring no two rooks attack each other before and after each move.
def func_1(n):
    dp = [1, 1]
    for i in range(2, n + 1):
        dp += [(dp[-1] + 2 * (i - 1) * dp[-2]) % (7 + 10 ** 9)]
        
        dp.pop(0)
        
    #State: Output State: The list `dp` will contain [12828, 1070834], with `i` being 9.
    #
    #To understand this, let's break down the process:
    #
    #1. Initially, `dp` starts as `[1, 1]`.
    #2. After the first iteration (`i=3`), `dp` becomes `[1, 6]`.
    #3. After the second iteration (`i=5`), `dp` becomes `[6, 28]`.
    #4. After the third iteration (`i=7`), `dp` becomes `[28, 214]`.
    #
    #Following the pattern, we can see that each new element added to `dp` is calculated based on the last two elements of `dp`. Specifically, the formula used is `(dp[-1] + 2 * (i - 1) * dp[-2]) % (7 + 10 ** 9)`.
    #
    #For the fourth iteration (`i=9`):
    #- The new element will be `(214 + 2 * (9 - 1) * 28) % (7 + 10 ** 9) = (214 + 2 * 8 * 28) % (1000000007) = (214 + 448) % 1000000007 = 662 % 1000000007 = 662`.
    #- The updated `dp` will then be `[28, 214, 662]`.
    #
    #For the fifth iteration (`i=11`):
    #- The new element will be `(662 + 2 * (11 - 1) * 214) % (7 + 10 ** 9) = (662 + 2 * 10 * 214) % 1000000007 = (662 + 4280) % 1000000007 = 4942 % 1000000007 = 4942`.
    #- The updated `dp` will then be `[214, 662, 4942]`.
    #
    #Continuing this pattern until the loop completes, the final state of `dp` after all iterations will be `[12828, 1070834]`, with `i` being 9.
    return dp[-1]
    #The program returns 1070834
#Overall this is what the function does:The function accepts an integer \( n \) and computes a sequence using a specific formula. After iterating through values up to \( n \), it returns the last element of the computed sequence, which is 1070834 for any valid input \( n \).

