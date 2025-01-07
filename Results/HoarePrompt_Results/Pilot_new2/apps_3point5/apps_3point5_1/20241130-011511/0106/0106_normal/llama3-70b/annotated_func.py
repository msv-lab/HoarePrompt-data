#State of the program right berfore the function call: **Precondition**: **n, m, k, a, b are positive integers such that 1 ≤ n, m, k ≤ 1000 and 1 ≤ a, b ≤ n·m·k.**
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
    #State of the program after the if-else block has been executed: *`n`, `m`, `k`, `a`, `b`, `a_floor`, `a_block`, `b_floor`, `b_block` remain the same. `min_block_time` is assigned the value of the minimum time between blocks, calculated as the minimum of the absolute difference between `a_block` and `b_block` and `n -` the absolute difference between `a_block` and `b_block`, multiplied by 15. If `a_floor` is greater than `b_floor`, `min_floor_time` is assigned the value of `(a_floor - b_floor) * 5 + 10`. If `a_floor` is not greater than `b_floor`, `min_floor_time` is assigned the value of `(b_floor - a_floor) * 5 + 10`.
    print(min_block_time + min_floor_time)
#Overall this is what the function does:The function `func` reads input for positive integers n, m, k, a, and b. It calculates the floor and block numbers for values a and b. Then, it determines the minimum time required to move between blocks and floors based on the calculated values. Finally, it prints the sum of the minimum block time and the minimum floor time. The function does not accept any parameters and does not have a return value.

