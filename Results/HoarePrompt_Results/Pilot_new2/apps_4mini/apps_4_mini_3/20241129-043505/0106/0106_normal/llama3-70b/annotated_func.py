#State of the program right berfore the function call: n, m, and k are positive integers such that 1 ≤ n, m, k ≤ 1000; a and b are distinct integers such that 1 ≤ a, b ≤ n·m·k.
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
    #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are integers. `a` and `b` are distinct integers satisfying 1 ≤ a, b ≤ n·m·k. If `a_floor` is greater than `b_floor`, then `min_floor_time` is equal to (a_floor - b_floor) * 5 + 10. Otherwise, `min_floor_time` is equal to (b_floor - a_floor) * 5 + 10, with `a_floor` being less than or equal to `b_floor`. In both cases, `min_block_time` is equal to min(abs(a_block - b_block), n - abs(a_block - b_block)) * 15.
    print(min_block_time + min_floor_time)
#Overall this is what the function does:The function calculates the minimum time needed for two distinct integers `a` and `b` to reach each other based on their positions calculated using the inputs `n`, `m`, and `k`. The function does not accept parameters directly but reads them from input. It computes the block and floor of both integers and considers the horizontal and vertical distance between them to determine the total time, which is then printed. It handles cases where `a` and `b` are at different floors and blocks, and always adds a base time of 10 minutes for the initial movement.

