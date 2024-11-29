#State of the program right berfore the function call: n, m, and k are positive integers such that 1 ≤ n, m, k ≤ 1000; a and b are integers such that 1 ≤ a, b ≤ n·m·k and a is not equal to b.
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
    #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are positive integers; `a` and `b` are integers equal to the first and second input values respectively; `a_floor` is equal to `(a - 1) % m + 1` and `b_floor` is equal to `(b - 1) % m + 1`; `a_block` is equal to `(a - 1) // (m * k) + 1` and `b_block` is equal to `(b - 1) // (m * k) + 1`; `min_block_time` is equal to `min(abs(a_block - b_block), n - abs(a_block - b_block)) * 15`; if `a_floor` is greater than `b_floor`, then `min_floor_time` is equal to `(a_floor - b_floor) * 5 + 10`; otherwise, `min_floor_time` is equal to `(b_floor - a_floor) * 5 + 10`.
    print(min_block_time + min_floor_time)
#Overall this is what the function does:The function accepts user input for three positive integers `n`, `m`, and `k`, and two integers `a` and `b`, calculates the minimum block time and floor time between two specified points (a and b) within a grid defined by `n`, `m`, and `k`, and prints the total time it takes to travel between those points. Specifically, it computes the block difference and the floor difference, with the total time being based on defined constants for block and floor travel. There are no explicit return values from the function; it only prints the calculated time.

