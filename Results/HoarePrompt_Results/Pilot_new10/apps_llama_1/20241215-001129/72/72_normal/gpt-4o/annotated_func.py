#State of the program right berfore the function call: n, m, k, x, and y are integers such that 1 <= n, m <= 100, 1 <= k <= 10^18, 1 <= x <= n, and 1 <= y <= m.
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
    #State of the program after the if block has been executed: *`n` equals `input_n`, `m` equals `input_m`, `k` equals `input_k`, `x` equals `input_x` - 1, `y` equals `input_y` - 1. If `n` > 1, then `full_cycles` equals `input_k // ((2 * input_n - 2) * input_m)`, `remaining_questions` equals `k % ((2 * n - 2) * m)`, `min_questions` equals `input_k // ((2 * input_n - 2) * input_m) // (2 * n - 2)`, and `max_questions` equals `(input_k // ((2 * input_n - 2) * input_m) + n - 1) // (2 * n - 2)`. If `n` is 1, then `full_cycles` equals `input_k // input_m`, `remaining_questions` equals `k % input_m`, and `min_questions` equals `max_questions` equals `full_cycles`.
    sergei_questions = min_questions
    if (x == 0 or x == n - 1) :
        sergei_questions = full_cycles // (2 * n - 2) + (full_cycles % (2 * n - 2) >= 1
    )
    else :
        sergei_questions = (full_cycles + x - 1) // (2 * n - 2) + (full_cycles % (2 *
    n - 2) >= x)
    #State of the program after the if-else block has been executed: `n` equals `input_n`, `m` equals `input_m`, `k` equals `input_k`, `x` equals `input_x` - 1, `y` equals `input_y` - 1. If `x` is 0 or `x` is `n - 1`, then `sergei_questions` equals `full_cycles // (2 * n - 2) + (full_cycles % (2 * n - 2) >= 1)`. Otherwise, `sergei_questions` equals `(full_cycles + input_x - 2) // (2 * n - 2) + (full_cycles % (2 * n - 2) >= input_x - 1)`. The conditions for `full_cycles`, `remaining_questions`, `min_questions`, `max_questions` based on `n` remain as initially stated, with the understanding that `n` must be greater than 1 for the `sergei_questions` update to apply when `x` is 0 or `x` is `n - 1`, and `x` is not equal to 0 and `x` is not equal to `n - 1` otherwise. If `n` > 1, then `full_cycles` equals `input_k // ((2 * input_n - 2) * input_m)`, `remaining_questions` equals `k % ((2 * n - 2) * m)`, `min_questions` equals `input_k // ((2 * input_n - 2) * input_m) // (2 * n - 2)`, `max_questions` equals `(input_k // ((2 * input_n - 2) * input_m) + n - 1) // (2 * n - 2)`. If `n` is 1, then `full_cycles` equals `input_k // input_m`, `remaining_questions` equals `k % input_m`, `min_questions` equals `max_questions` equals `full_cycles`.
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
        
    #State of the program after the  for loop has been executed: `n` equals `input_n`, `m` equals `input_m`, `k` equals `input_k`, `x` equals `input_x - 1`, `y` equals `input_y - 1`, `full_cycles`, `min_questions`, and `max_questions` are calculated based on `n`, `k`, and `m`, `row` and `direction` are updated based on the loop's boundary conditions, `max_questions` is the final value after incrementing or decrementing, `sergei_questions` is the final value after incrementing, `col` equals `m`, and `remaining_questions` equals 0.
    print(max_questions, min_questions, sergei_questions)
#Overall this is what the function does:The function accepts integers `n`, `m`, `k`, `x`, and `y` as input, calculates the number of questions that will be asked to Sergei, the minimum number of questions that can be asked, and the maximum number of questions that can be asked, and prints these values, handling edge cases such as when `n` is 1, and implicitly handling cases such as when `k` is 0, or when `x` or `y` is out of range, but without explicitly checking for invalid input values.

