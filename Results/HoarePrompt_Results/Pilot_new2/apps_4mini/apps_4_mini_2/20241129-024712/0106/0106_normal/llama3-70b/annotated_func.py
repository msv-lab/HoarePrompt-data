#State of the program right berfore the function call: n, m, and k are integers such that 1 ≤ n, m, k ≤ 1000, and a and b are integers such that 1 ≤ a, b ≤ n·m·k and a ≠ b.
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
    #State of the program after the if-else block has been executed: *`n`, `m`, `k` are user input integers; `a`, `b` are user input values. If `a_floor` is greater than `b_floor`, then `min_block_time` is equal to `min(abs(a_block - b_block), n - abs(a_block - b_block)) * 15` and `min_floor_time` is equal to `(a_floor - b_floor) * 5 + 10`. Otherwise, `min_block_time` is equal to `min(abs(a_block - b_block), n - abs(a_block - b_block)) * 15` and `min_floor_time` is equal to `(b_floor - a_floor) * 5 + 10`.
    print(min_block_time + min_floor_time)
#Overall this is what the function does:The function accepts user inputs for integers `n`, `m`, and `k` (with constraints 1 ≤ n, m, k ≤ 1000), and integers `a` and `b` (with constraints 1 ≤ a, b ≤ n·m·k and a ≠ b). It calculates the minimum time required to move between two specified blocks in a grid structure, taking into account both block and floor transitions, and prints the total time. The function does not return any values; it only prints the result.

