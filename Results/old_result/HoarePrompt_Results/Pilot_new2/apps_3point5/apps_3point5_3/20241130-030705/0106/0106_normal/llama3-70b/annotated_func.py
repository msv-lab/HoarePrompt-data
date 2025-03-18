#State of the program right berfore the function call: **Precondition**: **n, m, k, a, b are integers such that 1 ≤ n, m, k ≤ 1000, 1 ≤ a, b ≤ n·m·k, and a ≠ b.**
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
    #State of the program after the if-else block has been executed: *`n, m, k` are integers such that 1 ≤ n, m, k ≤ 1000, `a, b` are integers such that 1 ≤ a, b ≤ n·m·k and a ≠ b, `a` and `b` are assigned the values obtained by mapping integers from the input split, `a_floor` is equal to ((a - 1) % m) + 1, `a_block` is equal to (a - 1) // (m * k) + 1, `b_floor` is equal to (b - 1) % m + 1, `b_block` is equal to (b - 1) // (m * k) + 1, `min_block_time` is equal to the minimum value between the absolute difference of `a_block` and `b_block` and `n - abs(a_block - b_block)` multiplied by 15. If `a_floor` is greater than `b_floor`, `min_floor_time` is equal to (a_floor - b_floor) * 5 + 10. If `a_floor` is not greater than `b_floor`, `min_floor_time` is equal to (b_floor - a_floor) * 5 + 10.
    print(min_block_time + min_floor_time)
#Overall this is what the function does:The function `func` reads input values for `n`, `m`, `k`, `a`, and `b`. It calculates the time taken to move between two points based on the floors and blocks they are located on. The minimum block time is computed by finding the minimum distance between the blocks multiplied by 15. The minimum floor time is calculated based on the difference between the floors multiplied by 5 with an additional fixed time of 10. Finally, the total time taken for the movement is printed.

