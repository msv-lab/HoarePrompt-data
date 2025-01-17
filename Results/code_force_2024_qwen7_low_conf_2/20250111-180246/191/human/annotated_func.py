#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3⋅10^5 and 0 ≤ k ≤ n. The moves are represented as pairs of integers (r_i, c_i) such that 1 ≤ r_i, c_i ≤ n, and no two rooks attack each other, including the moves made by both the player and the computer.
def func_1():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        k = int(data[index + 1])
        
        index += 2
        
        rows = set()
        
        cols = set()
        
        for _ in range(k):
            r = int(data[index])
            c = int(data[index + 1])
            index += 2
            rows.add(r)
            cols.add(c)
            if r != c:
                rows.add(c)
                cols.add(r)
        
        free_rows = n - len(rows)
        
        free_cols = n - len(cols)
        
        m = min(free_rows, free_cols)
        
        result = 1
        
        for i in range(1, m + 1):
            result = result * i % MOD
        
        results.append(result)
        
    #State of the program after the  for loop has been executed: `t` is a non-negative integer, `n` is an integer such that 1 ≤ `n` ≤ 3⋅10^5, `k` is an integer such that 0 ≤ `k` ≤ `n`, `data` is a list of strings obtained from splitting the input, `index` is the final value of `index` after all iterations, `results` is a list containing the product of all integers from 1 to `m` modulo `MOD` for each iteration, where `m` is `min(n - len(rows), n - len(cols))`, `rows` is a set containing all unique row indices that were added during the iterations, `cols` is a set containing all unique column indices that were added during the iterations.
    for res in results:
        print(res)
        
    #State of the program after the  for loop has been executed: `t` is a non-negative integer, `n` is an integer such that \(1 \leq n \leq 3 \times 10^5\), `k` is an integer such that \(0 \leq k \leq n\), `data` is a list of strings obtained from splitting the input, `index` is the final value of `index` after all iterations, `results` is a list of products of all integers from 1 to `m` modulo `MOD` for each iteration where `m` is `min(n - len(rows), n - len(cols))`, `rows` is a set containing all unique row indices that were added during the iterations, `cols` is a set containing all unique column indices that were added during the iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a board size `n`, the number of rook moves `k`, and `k` pairs of row and column indices representing the moves. For each test case, it calculates the minimum number of moves required to place `k` non-attacking rooks on an `n x n` board such that no two rooks can attack each other either horizontally or vertically. It then computes the factorial of this minimum number of moves (`m`) modulo a constant `MOD` and appends the result to a list. After processing all test cases, it prints each result from the list.

