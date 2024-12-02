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
    #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are integers where 1 ≤ n, m, k ≤ 1000; `a` and `b` are integers where 1 ≤ a, b ≤ n·m·k and a ≠ b; `a_floor` is equal to `(a - 1) % m + 1`; `a_block` is equal to `(a - 1) // (m * k) + 1`; `b_floor` is equal to `(b - 1) % m + 1`; `b_block` is equal to `(b - 1) // (m * k) + 1`; `min_block_time` is equal to min(abs(a_block - b_block), n - abs(a_block - b_block)) * 15; if `a_floor` is greater than `b_floor`, then `min_floor_time` is equal to `(a_floor - b_floor) * 5 + 10`. Otherwise, `a_floor` is less than or equal to `b_floor`, and `min_floor_time` is equal to `(b_floor - a_floor) * 5 + 10.
    print(min_block_time + min_floor_time)
#Overall this is what the function does:The function accepts two integer pairs, n, m, k (1 ≤ n, m, k ≤ 1000) and a, b (1 ≤ a, b ≤ n·m·k, a ≠ b) from user input. It computes the minimum time taken to travel between two specified floors (derived from a and b) within a multi-block structure, where each block's time to move vertically is calculated based on the floor difference and the number of blocks. The total time is determined by the block movement time and the floor movement time, which is then printed. The function does not return a value but outputs the computed total time directly.

