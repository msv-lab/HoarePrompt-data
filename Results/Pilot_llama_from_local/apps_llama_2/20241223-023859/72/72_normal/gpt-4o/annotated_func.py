#State of the program right berfore the function call: n and m are positive integers, k is a non-negative integer, and x and y are positive integers such that 1 <= x <= n and 1 <= y <= m.
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
    #State of the program after the if block has been executed: `n` is a positive integer, `m` is a positive integer, `k` is a non-negative integer, `y` is a non-negative integer, `x` equals `x - 1`. If `n` is greater than 1, then `full_cycle_length` is `(2 * n - 2) * m`, `full_cycles` equals `k // ((2 * n - 2) * m)`, `remaining_questions` equals `k % ((2 * n - 2) * m)`, `min_questions` equals `k // ((2 * n - 2) * m)`, and `max_questions` equals `(k // ((2 * n - 2) * m) + n - 1) // (2 * n - 2)`. If `n` is 1, then `full_cycle_length` is `m`, `full_cycles` equals `k // m`, `remaining_questions` equals `k % m`, and both `min_questions` and `max_questions` equal `k // m`.
    sergei_questions = min_questions
    if (x == 0 or x == n - 1) :
        sergei_questions = full_cycles // (2 * n - 2) + (full_cycles % (2 * n - 2) >= 1
    )
    else :
        sergei_questions = (full_cycles + x - 1) // (2 * n - 2) + (full_cycles % (2 *
    n - 2) >= x)
    #State of the program after the if-else block has been executed: *`n` is a positive integer, `m` is a positive integer, `k` is a non-negative integer, `y` is a non-negative integer. If `n` is greater than 1, then `full_cycle_length` is `(2 * n - 2) * m`, `full_cycles` equals `k // ((2 * n - 2) * m)`, `remaining_questions` equals `k % ((2 * n - 2) * m)`, `min_questions` equals `k // ((2 * n - 2) * m)`, `max_questions` equals `(k // ((2 * n - 2) * m) + n - 1) // (2 * n - 2)`. If `x` is either 0 or `n - 1`, then `sergei_questions` equals `full_cycles // (2 * n - 2) + (full_cycles % (2 * n - 2) >= 1)`. If `x` is not equal to 0 and not equal to `n - 1`, then `sergei_questions` equals `(k // ((2 * n - 2) * m) + x - 1) // (2 * n - 2) + (k // ((2 * n - 2) * m) % (2 * n - 2) >= x)`. If `n` is 1, then `full_cycle_length` is `m`, `full_cycles` equals `k // m`, `remaining_questions` equals `k % m`, `min_questions` equals `k // m`, `max_questions` equals `k // m`. If `x` is either 0 or `n - 1`, the update formula for `sergei_questions` as provided does not apply due to division by zero, however since `n` equals 1 and `x` is either 0 or `n-1` which is also 0, then `sergei_questions` equals `k // m`. If `x` is not equal to 0 and not equal to `n - 1` but `n` equals 1, then this case is impossible because `n` equals 1, and `x` cannot be other than 0, hence this case does not affect the result.
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
        
    #State of the program after the  for loop has been executed: `n` and `m` are positive integers, `k` is a non-negative integer, `y` and `x` are non-negative integers, `row` is between 0 and `n-1`, `direction` is either 1 or -1, `max_questions` is updated based on the net movement, `sergei_questions` is the initial value plus the number of encounters with `(x, y)`, and `remaining_questions` is 0.
    print(max_questions, min_questions, sergei_questions)
#Overall this is what the function does:The function calculates and prints three values related to the movement of an object within a grid of size n by m, where n and m are positive integers. The movement is determined by the number of steps k, with the object initially at position (x, y), where x and y are positive integers within the ranges 1 to n and 1 to m, respectively. The three calculated values are: max_questions, which represents the maximum number of questions that can be asked; min_questions, which represents the minimum number of questions that can be asked; and sergei_questions, which represents the number of times the object encounters its initial position. The function handles edge cases, such as when n is 1, where the object moves only horizontally, and when x is either 0 or n-1, where the object's movement is affected by the grid boundaries. The function also accounts for the object's direction of movement, which changes when it reaches the grid boundaries. The function prints the calculated values of max_questions, min_questions, and sergei_questions, providing insight into the object's movement and encounters within the grid.

