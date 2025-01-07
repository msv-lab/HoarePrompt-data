#State of the program right berfore the function call: n, m, and k are integers such that 1 ≤ n, m, k ≤ 1000; a and b are integers such that 1 ≤ a, b ≤ n·m·k and a ≠ b.
def func():
    n, m, k = map(int, input().split())
    a, b = map(int, input().split())
    a_floor = (a - 1) % m + 1
    a_block = (a - 1) // (m * k) + 1
    b_floor = (b - 1) % m + 1
    b_block = (b - 1) // (m * k) + 1
    min_block_time = min(abs(a_block - b_block), n - abs(a_block - b_block)) * 15
    if (a_floor > b_floor) :
        min_floor_time = (a_floor - b_floor) * 5 + 10
    else :
        min_floor_time = (b_floor - a_floor) * 5 + 10
    #State of the program after the if-else block has been executed: *`n`, `m`, `k` are integers assigned based on input values. `a` and `b` are integers between 1 and `n·m·k`, with `a` ≠ `b`. The values of `a_floor` and `b_floor` are determined by the formulas `(a - 1) % m + 1` and `(b - 1) % m + 1`, respectively, and the values of `a_block` and `b_block` are calculated as `(a - 1) // (m * k) + 1` and `(b - 1) // (m * k) + 1`. If `a_floor` is greater than `b_floor`, then `min_floor_time` is calculated as `(a_floor - b_floor) * 5 + 10`. Otherwise, if `a_floor` is not greater than `b_floor`, then `min_floor_time` is calculated as `(b_floor - a_floor) * 5 + 10`. In both cases, `min_block_time` is defined as `min(abs(a_block - b_block), n - abs(a_block - b_block)) * 15`.
    print(min_block_time + min_floor_time)
#Overall this is what the function does:The function accepts two pairs of integers `n`, `m`, `k` and `a`, `b` from user input. It calculates the minimum time required to travel between two points represented by `a` and `b` in a grid-like system defined by `n` blocks each containing `m` floors and `k` segments. The function returns the sum of the minimum block travel time and the minimum floor travel time, accounted for different scenarios of block positions and floor levels. It does not handle any edge cases related to invalid inputs or scenarios where `a` is equal to `b`, but it is defined that `a` and `b` will always be distinct based on the preconditions.

