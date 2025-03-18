#State of the program right berfore the function call: 
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
    #State of the program after the if-else block has been executed: *`n`, `m`, `k`, `a`, `b` are integers representing the input values. `a_floor`, `a_block`, `b_floor`, `b_block`, `min_block_time` are calculated based on the input values. If `a_floor > b_floor`, the function calculates `min_block_time` as the minimum of absolute value of `(a_block - b_block)` and `n - abs(a_block - b_block)` multiplied by 15. Additionally, `min_floor_time` is determined as `(a_floor - b_floor) * 5 + 10`. If `a_floor <= b_floor`, `min_floor_time` is calculated as `(b_floor - a_floor) * 5 + 10`.
    print(min_block_time + min_floor_time)
#Overall this is what the function does:The function `func` reads input values and calculates the minimum time required to move between blocks and floors based on the given input. It then prints the sum of the time taken between blocks and floors. The function does not accept any parameters and does not return any value.

