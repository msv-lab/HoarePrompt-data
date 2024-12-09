#State of the program right berfore the function call: n and m are integers between 1 and 100 inclusive, k is a positive integer up to 10^18, x is an integer between 1 and n inclusive, and y is an integer between 1 and m inclusive.
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
    #State of the program after the if block has been executed: *`n` is an integer between 1 and 100 inclusive, `m` is an integer between 1 and 100 inclusive, `k` is a positive integer up to 10^18, `x` is between 0 and `n-1`, `y` is between 0 and `m-1`. If `n` > 1, then `full_cycle_length` is equal to (2 * n - 2) * m, `full_cycles` is equal to k // ((2 * n - 2) * m), `remaining_questions` is equal to k % ((2 * n - 2) * m), `min_questions` is equal to `full_cycles // (2 * n - 2)`, and `max_questions` is equal to (`full_cycles` + n - 1) // (2 * n - 2). If `n` is equal to 1, no changes occur in the state of `min_questions` and `max_questions`.
    sergei_questions = min_questions
    if (x == 0 or x == n - 1) :
        sergei_questions = full_cycles // (2 * n - 2) + (full_cycles % (2 * n - 2) >= 1
    )
    else :
        sergei_questions = (full_cycles + x - 1) // (2 * n - 2) + (full_cycles % (2 *
    n - 2) >= x)
    #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 100 inclusive, `m` is an integer between 1 and 100 inclusive, `k` is a positive integer up to 10^18, `x` is between 0 and `n-1`, `y` is between 0 and `m-1`, and `sergei_questions` is equal to `full_cycles // (2 * n - 2) + (full_cycles % (2 * n - 2) >= 1)` if `x` is 0 or `n - 1`. Otherwise, if `x` is between 1 and `n-2`, `sergei_questions` is updated to `(full_cycles + x - 1) // (2 * n - 2) + (full_cycles % (2 * n - 2) >= x)`.
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
        
    #State of the program after the  for loop has been executed: `n` is between 1 and 100 inclusive, `m` is between 1 and 100 inclusive, `k` is a positive integer up to 10^18, `x` is between 0 and `n-1`, `y` is between 0 and `m-1`, `row` oscillates between 0 and `n-1` based on the direction of movement, `col` is equal to `m - 1`, `sergei_questions` reflects the total number of matches found during all iterations, `direction` is either 1 or -1 depending on the final oscillation, `remaining_questions` is less than or equal to 0, and `max_questions` reflects the net result of increments and decrements throughout the loop execution. If the loop did not execute, `sergei_questions` remains unchanged, `max_questions` remains unchanged, and `row` stays at its initial value.
    print(max_questions, min_questions, sergei_questions)
#Overall this is what the function does:The function accepts five parameters: integers `n`, `m`, and `k` (where `n` and `m` are between 1 and 100 inclusive, and `k` is a positive integer up to 10^18), and integers `x` and `y` (where `x` is between 1 and `n` inclusive, and `y` is between 1 and `m` inclusive). It calculates the number of questions Sergei can answer based on the number of full cycles completed in `k` steps, and how many remaining steps are left. The function returns the maximum and minimum number of questions Sergei can answer, as well as the actual number of questions he answers at the specified position `(x, y)` during the process. The calculations consider the direction of movement (up and down) within the range defined by `n` and `m`, and handle cases where `n` equals 1 differently from cases where it is greater than 1.

