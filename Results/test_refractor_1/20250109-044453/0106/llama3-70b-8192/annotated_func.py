#State of the program right berfore the function call: n, m, k are positive integers such that 1 ≤ n, m, k ≤ 1000, a and b are integers such that 1 ≤ a, b ≤ n·m·k and a ≠ b.
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
    #State of the program after the if-else block has been executed: *`a`, `b`, `m`, `a_floor`, `a_block`, `b_floor`, `b_block`, `min_block_time`, and `min_floor_time` are as follows: if `a_floor > b_floor`, then `min_floor_time` is \((a_floor - b_floor) * 5 + 10\). Otherwise, `min_floor_time` is \((b_floor - a_floor) * 5 + 10\). `min_block_time` remains unchanged from its initial value.
    print(min_block_time + min_floor_time)
#Overall this is what the function does:The function calculates and returns the minimum time required for two people to meet at a given location. The function takes five parameters: `n`, `m`, `k`, `a`, and `b`. Here, `n`, `m`, and `k` are positive integers between 1 and 1000, representing dimensions and blocks, while `a` and `b` are integers between 1 and \(n \cdot m \cdot k\) representing the starting positions of the two people, with the condition that `a ≠ b`.

First, the function computes the floor and block indices for both `a` and `b` based on the given values of `m` and `k`. The floor index represents the position within the current block, and the block index represents the block number. It then calculates the minimum time required to move between the blocks (`min_block_time`) and the minimum time required to move within the same block (`min_floor_time`). If `a_floor > b_floor`, `min_floor_time` is calculated as \((a_floor - b_floor) * 5 + 10\); otherwise, it is calculated as \((b_floor - a_floor) * 5 + 10\).

Finally, the function prints the sum of `min_block_time` and `min_floor_time`, which represents the total minimum time required for the two people to meet. Potential edge cases include scenarios where `a` and `b` are in the same block, and the function correctly handles these by only calculating the necessary time to move within the block.

The function does not return any value explicitly; instead, it prints the result.

