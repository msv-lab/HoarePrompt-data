#State of the program right berfore the function call: n, m, k are positive integers such that 1 ≤ n, m, k ≤ 1000, a and b are positive integers such that 1 ≤ a, b ≤ n·m·k and a ≠ b.
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
    #State of the program after the if-else block has been executed: *`n`, `m`, `k`, `a`, `b`, `a_floor`, `a_block`, `b_floor`, `b_block`, and `min_block_time` are as follows: 
    #- If `a_floor > b_floor`, then `min_floor_time` = (a_floor - b_floor) * 5 + 10.
    #- If `a_floor <= b_floor`, then `min_floor_time` = (b_floor - a_floor) * 5 + 10.
    #- `min_block_time` is determined based on the conditions provided in each branch: 
    #  - If `a_floor > b_floor`, then `min_block_time` = (abs(a_block - b_block), n - abs(a_block - b_block)) * 15.
    #  - If `a_floor <= b_floor`, then `min_block_time` = max(0, (abs(a_block - b_block) - 1) * 15, (n - abs(a_block - b_block) - 1) * 15).
    print(min_block_time + min_floor_time)
#Overall this is what the function does:The function accepts five parameters: \( n \), \( m \), \( k \), \( a \), and \( b \), where \( n \), \( m \), and \( k \) are positive integers such that \( 1 \leq n, m, k \leq 1000 \), and \( a \) and \( b \) are positive integers such that \( 1 \leq a, b \leq n \cdot m \cdot k \) and \( a \neq b \). It calculates and prints the minimum time required for two entities to meet, given the constraints of moving between floors and blocks. The function first computes the floor and block positions for both \( a \) and \( b \). It then determines the minimum time required to move vertically (floors) and horizontally (blocks) between the two entities, considering the shortest path. Finally, it prints the total time, which is the sum of the minimum floor time and the minimum block time. Potential edge cases include when \( a \) and \( b \) are in the same block but on different floors, and when they are in the same floor but on different blocks. The function handles these cases appropriately by calculating the absolute difference in positions and applying the respective movement times.

