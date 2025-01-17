#State of the program right berfore the function call: n, m, k are positive integers such that 1 ≤ n, m, k ≤ 1000, and a and b are integers such that 1 ≤ a, b ≤ n·m·k and a ≠ b.
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
    #State of the program after the if-else block has been executed: `n`, `m`, `k`, `a`, `b`, `a_floor`, `a_block`, `b_floor`, `b_block`, `min_block_time`, and `min_floor_time` are integers. If `a_floor` is greater than `b_floor`, then `min_floor_time` is `(a_floor - b_floor) * 5 + 10` and `min_block_time` remains the minimum of (absolute difference between `a_block` and `b_block`, `n` minus this absolute difference) multiplied by 15. Otherwise, `min_floor_time` is `(b_floor - a_floor) * 5 + 10` and `min_block_time` remains the same.
    print(min_block_time + min_floor_time)
#Overall this is what the function does:The function accepts four positive integers `n`, `m`, `k`, and two distinct integers `a` and `b` within the range \(1 \leq a, b \leq n \cdot m \cdot k\). It calculates and prints the total time required for `a` and `b` to meet under the given constraints. The total time is composed of the minimum time to travel between the floors (`min_floor_time`) and the minimum time to travel between the blocks (`min_block_time`). 

- The floor calculation considers the vertical distance between `a` and `b` and adds a fixed time of 10 minutes for the elevator to reach the ground floor.
- The block calculation considers the horizontal distance between the blocks where `a` and `b` are located and multiplies it by 15 minutes, which is the time it takes to move between adjacent blocks.

The function handles the case where `a_floor` might be greater than `b_floor` and adjusts the floor travel time accordingly. There are no explicit edge cases mentioned in the code; however, the code assumes that `a` and `b` are within the valid range and that `a` is not equal to `b`. If these conditions are not met, the function may behave unpredictably.

