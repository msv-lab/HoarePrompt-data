#State of the program right berfore the function call: n and m are non-negative integers such that 1 <= n <= 100 and 1 <= m <= 100, k is a non-negative integer such that 1 <= k <= 10^18, x is a non-negative integer such that 1 <= x <= n, and y is a non-negative integer such that 1 <= y <= m.
def func():
    n, m, k, x, y = map(int, input().split())
    x -= 1
    y -= 1
    full_cycle_length = (2 * n - 2) * m if n > 1 else m
    full_cycles = k // full_cycle_length
    remaining_questions = k % full_cycle_length
    min_questions = full_cycles
    max_questions = full_cycles
    if (n > 1) :
        min_questions = full_cycles // (2 * n - 2)
        max_questions = (full_cycles + n - 1) // (2 * n - 2)
    #State of the program after the if block has been executed: `n` is an input integer, `m` is an input integer, `k` is an input integer, `x` is an input integer minus 1, `y` is an input integer minus 1. If `n` is greater than 1, then `full_cycle_length` is `(2 * n - 2) * m`, `full_cycles` is `k // ((2 * n - 2) * m)`, `remaining_questions` is `k % ((2 * n - 2) * m)`, `min_questions` is `k // ((2 * n - 2) * m)`, and `max_questions` is `(k // ((2 * n - 2) * m) + n - 1) // (2 * n - 2)`. If `n` is not greater than 1, then `full_cycle_length` is `m`, `full_cycles` is `k // m`, `remaining_questions` is `k % m`, and both `min_questions` and `max_questions` are `k // m`.
    sergei_questions = min_questions
    if (x == 0 or x == n - 1) :
        sergei_questions = full_cycles // (2 * n - 2) + (full_cycles % (2 * n - 2) >= 1
    )
    else :
        sergei_questions = (full_cycles + x - 1) // (2 * n - 2) + (full_cycles % (2 *
    n - 2) >= x)
    #State of the program after the if-else block has been executed: `n` is an input integer, `m` is an input integer, `k` is an input integer, `x` is an input integer minus 1, `y` is an input integer minus 1. If `n` is greater than 1, then `full_cycle_length` is `(2 * n - 2) * m`, `full_cycles` is `k // ((2 * n - 2) * m)`, `remaining_questions` is `k % ((2 * n - 2) * m)`, `min_questions` is `k // ((2 * n - 2) * m)`, `max_questions` is `(k // ((2 * n - 2) * m) + n - 1) // (2 * n - 2)`, and `sergei_questions` is determined based on whether `x` equals 0 or `n-1` or not. If `x` equals 0 or `n-1`, then `sergei_questions` is `k // ((2 * n - 2) * m)`, otherwise, `sergei_questions` is `(full_cycles + x - 1) // (2 * n - 2) + (full_cycles % (2 * n - 2) >= x)`. If `n` is not greater than 1, then `full_cycle_length` is `m`, `full_cycles` is `k // m`, `remaining_questions` is `k % m`, `min_questions` is `k // m`, `max_questions` is `k // m`, and `sergei_questions` is `k // m`.
    row = 0
    direction = 1
    for _ in range(remaining_questions):
        for col in range(m):
            if row == x and col == y:
                sergei_questions += 1
            if direction == 1:
                max_questions += 1
                row += direction
                if row == n:
                    direction = -1
                    row -= 2
            else:
                max_questions -= 1
                row += direction
                if row == -1:
                    direction = 1
                    row += 2
        
    #State of the program after the  for loop has been executed: `remaining_questions` is 0, `row` and `direction` are determined by the last iteration's operations regarding `n` and the loop's path, `max_questions` reflects the net effect of `direction` changes, and `sergei_questions` is the original value plus the occurrences where `row` equals `x` and `col` equals `y` during the loop, with other variables retaining their last updated or initial values based on the conditions provided.
    print(max_questions, min_questions, sergei_questions)
#Overall this is what the function does:The function calculates and prints the minimum, maximum, and Sergei's questions after a series of operations based on the input parameters n, m, k, x, and y. It determines the number of full cycles and remaining questions, then updates the questions based on the position of x and y within the cycle. The function handles different cases depending on the values of n and x, and iterates through the remaining questions to update the questions counts. The final output includes the maximum, minimum, and Sergei's questions. The function accepts parameters n and m (non-negative integers between 1 and 100), k (a non-negative integer between 1 and 10^18), and x and y (non-negative integers within the ranges of n and m respectively), and returns the calculated questions counts. The function's state after execution includes the updated values of max_questions, min_questions, and sergei_questions, which are printed as output. The function handles edge cases such as n being greater than 1 and x being 0 or n-1, and calculates the questions counts accordingly.

