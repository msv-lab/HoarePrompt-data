#State of the program right berfore the function call: n, m, k are positive integers such that 1 ≤ n, m, k ≤ 1000; a and b are integers such that 1 ≤ a, b ≤ n·m·k and a ≠ b.
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
    #State of the program after the if-else block has been executed: *`n`, `m`, `k` are positive integers such that 1 ≤ n, m, k ≤ 1000; `a`, `b` are integers such that 1 ≤ a, b ≤ n·m·k and a ≠ b; `a_floor`, `a_block`, `b_floor`, `b_block` are integers; `min_block_time` is an integer. If `a_floor > b_floor`, then `min_floor_time` is `(a_floor - b_floor) * 5 + 10`. Otherwise, `min_floor_time` is `(b_floor - a_floor) * 5 + 10`.
    print(min_block_time + min_floor_time)
#Overall this is what the function does:The function calculates the minimum time required for two people to meet at a specific location based on their positions and movement rules. It first determines the floor and block numbers for both individuals and computes the minimum block time and minimum floor time required for them to meet. If the floor number of one person is greater than the other, it calculates the additional time needed to move down the floor. Finally, it prints the total time as the sum of the block time and floor time. The function does not return anything but prints the result directly. Potential edge cases include when `a` and `b` are the same (which should not happen according to the constraints) or when the input values are out of the specified range (though the code handles this through the constraints). There is no missing functionality noted in the provided code.

