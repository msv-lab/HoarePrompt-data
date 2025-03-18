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
    #State: `a_floor` is equal to (a - 1) % m + 1, `a_block` is ((a - 1) // (m * k)) + 1, `b_floor` is (b - 1) % m + 1, `b_block` is (b - 1) // (m * k) + 1, `min_block_time` is calculated as min(abs(a_block - b_block), n - abs(a_block - b_block)) * 15, `min_floor_time` is either (a_floor - b_floor) * 5 + 10 if `a_floor` > `b_floor`, or (b_floor - a_floor) * 5 + 10 if `a_floor` ≤ `b_floor`, `n`, `m`, `k` are assigned values from input split and converted to integers, `a` and `b` are integers from input with 1 ≤ a, b ≤ n·m·k and a ≠ b.
    print(min_block_time + min_floor_time)
#Overall this is what the function does:The function calculates the minimum time required for two people to meet in a grid-based structure. It takes no parameters and reads values for `n`, `m`, `k`, `a`, and `b` from standard input, where `n` and `m` are dimensions of the grid, `k` represents the number of blocks in each floor, and `a` and `b` are positions of two people in the grid. The function then determines the minimum time needed for these two people to meet, considering both block traversal and floor traversal times. The final output is the total minimum time in seconds, which is printed to standard output. Potential edge cases include when `a` and `b` are in the same block but on different floors, or when they are in the same position. The function assumes `a` and `b` are within the valid range and `a` is not equal to `b`. If `a` and `b` are in the same block, the function only calculates the floor traversal time, which is not explicitly mentioned in the annotations.

