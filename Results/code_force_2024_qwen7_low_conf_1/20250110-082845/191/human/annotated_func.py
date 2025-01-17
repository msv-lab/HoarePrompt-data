#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are positive integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 0 ≤ k ≤ n. Additionally, r_i and c_i are integers such that 1 ≤ r_i, c_i ≤ n, and no two rooks attack each other based on the described rules.
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
        
    #State of the program after the  for loop has been executed: `t` is a positive integer, `n` is a positive integer, `results` is a list containing the product of all integers from 1 to `m` modulo `MOD` for each iteration, where `m` is the minimum of `n - len(rows)` and `n - len(cols)` for each iteration, `rows` is a set containing all unique row indices `r` and column indices `c` encountered during all loop iterations, `cols` is a set containing all unique column indices `c` and row indices `r` encountered during all loop iterations, `index` is the final value of `index` after all iterations (`val + 2 * t`), `k` is the total number of pairs processed during all iterations, `free_rows` is `n - len(rows)`, `free_cols` is `n - len(cols)`, `m` is the minimum of `free_rows` and `free_cols`.
    for res in results:
        print(res)
        
    #State of the program after the  for loop has been executed: `results` is a list containing the product of all integers from 1 to `m` modulo `MOD` for each iteration, where `m` is the minimum of `n - len(rows)` and `n - len(cols)` for each iteration, `rows` is a set containing all unique row indices `r` and column indices `c` encountered during all loop iterations, `cols` is a set containing all unique column indices `c` and row indices `r` encountered during all loop iterations, `index` is the final value of `index` after all iterations (`val + 2 * t`), `k` is the total number of pairs processed during all iterations, `free_rows` is `n - len(rows)`, `free_cols` is `n - len(cols)`, `m` is the minimum of `free_rows` and `free_cols`, and the loop executes at least `len(results)` times.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer `n` (the size of the board), an integer `k` (the number of rook pairs), and pairs of integers `r_i` and `c_i` (representing row and column indices of rooks). For each test case, it calculates the minimum number of non-attacking rooks that can be placed on the board by considering the available rows and columns after placing the given rook pairs. It then computes the product of all integers from 1 to this minimum number modulo a constant `MOD` and stores these results in a list. Finally, it prints each result from the list. The function handles edge cases where the number of available rows or columns might be zero and ensures that no two rooks attack each other based on the given rules.

