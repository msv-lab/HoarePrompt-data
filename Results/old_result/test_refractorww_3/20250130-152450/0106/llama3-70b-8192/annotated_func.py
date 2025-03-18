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
    #State: Postcondition: `a_floor` is `(a - 1) % m + 1`, `a_block` is `(a - 1) // (m * k) + 1`, `b_floor` is `(b - 1) % m + 1`, `b_block` is `(b - 1) // (m * k) + 1`, `min_block_time` is calculated as the minimum of the absolute difference between `a_block` and `b_block` multiplied by 15, or the difference between `n` and the absolute difference between `a_block` and `b_block` multiplied by 15, and `min_floor_time` is either `(a_floor - b_floor) * 5 + 10` if `a_floor > b_floor`, or `(b_floor - a_floor) * 5 + 10` otherwise.
    print(min_block_time + min_floor_time)
#Overall this is what the function does:The function processes two given integers \(a\) and \(b\) (where \(1 \leq a, b \leq n \cdot m \cdot k\) and \(a \neq b\)) along with positive integers \(n\), \(m\), and \(k\) (such that \(1 \leq n, m, k \leq 1000\)). It calculates and prints the total time required for two people to meet based on their positions in a grid-like structure. The total time consists of the minimum block travel time and the minimum floor travel time. The block travel time is determined by the minimum of the direct distance or the wrap-around distance between the blocks containing \(a\) and \(b\), each multiplied by 15 minutes. The floor travel time is determined by the vertical distance between the floors containing \(a\) and \(b\), plus a fixed 10-minute overhead. If \(a\) is on a higher floor than \(b\), the vertical distance is calculated as \(a\_floor - b\_floor\); otherwise, it is \(b\_floor - a\_floor\). The function handles the case where \(a\) and \(b\) are in the same block by setting the block travel time to 0. If \(a\) and \(b\) are in the same floor, the floor travel time is also 0.

