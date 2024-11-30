#State of the program right berfore the function call: n, m, k, a, b are all integers such that 1 ≤ n, m, k, a, b ≤ 1000, and a ≠ b.**
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
    #State of the program after the if-else block has been executed: *`n`, `m`, `k` are integers such that 1 ≤ n, m, k ≤ 1000, `a`, `b` are integers obtained from the input split, `a_floor` is equal to the remainder of (a - 1) divided by m plus 1, `a_block` is calculated as specified above, `b_floor` is calculated as (b - 1) % m + 1, `b_block` is calculated as (b - 1) // (m * k) + 1, `min_block_time` is assigned the minimum value between the absolute difference of a_block and b_block or n minus the absolute difference of a_block and b_block, multiplied by 15. After the if part executes, if `a_floor` is greater than `b_floor`, `min_floor_time` is calculated as (a_floor - b_floor) * 5 + 10. If the else part executes, `a_floor` is less than or equal to `b_floor`, and `min_floor_time` is calculated as (b_floor - a_floor) * 5 + 10.
    print(min_block_time + min_floor_time)
#Overall this is what the function does:The function `func` reads input values for n, m, k, a, b, and performs calculations based on these values. It calculates `a_floor` and `a_block` based on the input, then calculates `b_floor` and `b_block`. It determines `min_block_time` as the minimum time between blocks multiplied by 15. Additionally, it calculates `min_floor_time` based on the floors of a and b. The function then prints the sum of `min_block_time` and `min_floor_time`. It handles cases where a_floor is greater than b_floor and vice versa to calculate the appropriate `min_floor_time`. The function does not return any value.

