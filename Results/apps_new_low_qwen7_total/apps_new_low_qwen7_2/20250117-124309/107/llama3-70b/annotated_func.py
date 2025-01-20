#State of the program right berfore the function call: n, m, k are positive integers such that 1 <= n, m, k <= 1000; a and b are positive integers such that 1 <= a, b <= n * m * k and a != b.
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
    #State of the program after the if-else block has been executed: `n` is a positive integer, `m` is a positive integer, `k` is a positive integer, `a` is a positive integer, `b` is a positive integer, `a_floor` is a positive integer, `a_block` is calculated based on `a`, `b_floor` is a positive integer, `b_block` is calculated based on `b`, `min_block_time` is calculated based on `a` and `b`. If `a_floor` is greater than `b_floor`, then `min_floor_time` is `(a_floor - b_floor) * 5 + 10`. Otherwise, `min_floor_time` is `(b_floor - a_floor) * 5 + 10`. The values of `n`, `m`, `k`, `a`, `b`, `a_floor`, `a_block`, `b_floor`, `b_block`, and `min_block_time` remain unchanged from their initial states.
    print(min_block_time + min_floor_time)
#Overall this is what the function does:The function reads four positive integers \(n\), \(m\), \(k\), \(a\), and \(b\) from standard input, where \(1 \leq n, m, k \leq 1000\) and \(1 \leq a, b \leq n \times m \times k\) with \(a \neq b\). It calculates the minimum time required for two entities to meet, considering both block and floor traversal times. Specifically, it computes the time to traverse between the blocks containing \(a\) and \(b\) and the time to traverse between the floors within those blocks. The function then prints the total time required for the entities to meet. The function does not return any value.

