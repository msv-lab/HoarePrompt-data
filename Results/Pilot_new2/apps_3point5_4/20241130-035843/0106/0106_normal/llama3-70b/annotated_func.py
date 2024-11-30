#State of the program right berfore the function call: **Precondition**: **n, m, k, a, b are integers such that 1 ≤ n, m, k ≤ 1000 and 1 ≤ a, b ≤ n·m·k.**
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
    #State of the program after the if-else block has been executed: *`n`, `m`, `k`, `a`, `b`, `a_floor`, `a_block`, `b_floor`, `b_block`, `min_block_time`, `min_floor_time` remain the same. If `a_floor` > `b_floor`, `min_floor_time` is calculated as `(a_floor - b_floor) * 5 + 10`. If `a_floor` is less than or equal to `b_floor`, `min_floor_time` is calculated as `(b_floor - a_floor) * 5 + 10`.
    print(min_block_time + min_floor_time)
#Overall this is what the function does:Functionality: The function `func` reads input integers `n, m, k, a, b` satisfying the constraints 1 ≤ n, m, k ≤ 1000 and 1 ≤ a, b ≤ n·m·k. It then calculates `a_floor`, `a_block`, `b_floor`, `b_block`, `min_block_time`, and `min_floor_time` based on these inputs. `min_block_time` is determined by the difference in blocks multiplied by 15. `min_floor_time` is set based on the difference in floors multiplied by 5 with an additional fixed time. The function then prints the sum of `min_block_time` and `min_floor_time`. The function does not explicitly return any value.

