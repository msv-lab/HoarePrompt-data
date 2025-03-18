#State of the program right berfore the function call: n, m, k, x, and y are integers such that 1 ≤ n, m ≤ 100, 1 ≤ k ≤ 10^18, and 1 ≤ x ≤ n, 1 ≤ y ≤ m.
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
    #State of the program after the if block has been executed: *`n` is an integer greater than 1, `m` is an integer, `k` is an integer, `full_cycle_length` is `(2 * n - 2) * m`, `full_cycles` is `k // full_cycle_length`, `remaining_questions` is `k % full_cycle_length`, `min_questions` is `(k // full_cycle_length) // (2 * n - 2)`, `max_questions` is `(k // full_cycle_length + n - 1) // (2 * n - 2)`
    sergei_questions = min_questions
    if (x == 0 or x == n - 1) :
        sergei_questions = full_cycles // (2 * n - 2) + (full_cycles % (2 * n - 2) >= 1
    )
    else :
        sergei_questions = (full_cycles + x - 1) // (2 * n - 2) + (full_cycles % (2 *
    n - 2) >= x)
    #State of the program after the if-else block has been executed: *`n` is an integer greater than 1, `m` is an integer, `k` is an integer, `full_cycle_length` is `(2 * n - 2) * m`, `full_cycles` is `k // full_cycle_length`, `remaining_questions` is `k % full_cycle_length`, `min_questions` is `(k // full_cycle_length) // (2 * n - 2)`, `max_questions` is `(k // full_cycle_length + n - 1) // (2 * n - 2)`, `sergei_questions` is updated as follows: if `x` is either 0 or `n - 1`, then `sergei_questions` is `full_cycles // (2 * n - 2)`. Otherwise, `sergei_questions` is `(full_cycles + x - 1) // (2 * n - 2) + (full_cycles % (2 * n - 2) >= x)`
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
        
    #State of the program after the  for loop has been executed: `remaining_questions` is 0, `m` is the number of columns, `col` is `m`, `max_questions` is the sum of all increments minus all decrements, `sergei_questions` is incremented based on the condition `row == x and col == y`, `row` is the final value of `row`, `direction` is the final value of `direction`.
    print(max_questions, min_questions, sergei_questions)
#Overall this is what the function does:The function processes inputs `n`, `m`, `k`, `x`, and `y` which represent grid dimensions and a number of questions, respectively. It calculates the minimum and maximum number of questions Sergei can answer. Based on the position `x` and `y`, it updates the count of questions Sergei can answer. Finally, it prints the maximum, minimum, and updated count of questions Sergei can answer.

