#State of the program right berfore the function call: n, m, k are positive integers such that 1 <= n, m, k <= 1000, a and b are integers such that 1 <= a, b <= n*m*k and a != b.
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
    #State of the program after the if-else block has been executed: *`n` is 3, `m` is 2, `k` is 4, `a` is 7, `b` is 11, `a_floor` is 2, `a_block` is 1, `b_floor` is 1, `b_block` is 2, `min_block_time` is 15, `min_floor_time` is either 15 or 5 depending on whether `a_floor` is greater than `b_floor`.
    print(min_block_time + min_floor_time)
#Overall this is what the function does:The function calculates and returns the minimum time required for two people to meet at the same location in a grid-based system. The grid is divided into blocks and floors. The function takes inputs for the dimensions of the grid (n, m, k), and the starting positions of two people (a, b). It then computes the minimum time needed for them to meet, considering both the time taken to move between blocks and floors. The function does not accept any parameters and instead reads inputs from standard input. The final state of the program after the function concludes is that it prints the minimum total time required for the two people to meet. Potential edge cases include when `a` or `b` might be exactly on the boundary between blocks or floors, which the current code handles correctly.

