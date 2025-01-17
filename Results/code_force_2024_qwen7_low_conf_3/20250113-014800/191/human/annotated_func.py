#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3⋅10^5 and 0 ≤ k ≤ n. The values of r_i and c_i for each of the k lines are integers such that 1 ≤ r_i, c_i ≤ n.
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
        
    #State of the program after the  for loop has been executed: `t` is the number of times the outer loop was executed, `n` is the last value of `n` set during any iteration of the outer loop, `k` is the total number of inner iterations performed across all outer iterations, `data` is the list of strings from the input, `index` is the final value of `index` after the last iteration, `results` is a list containing the computed results for each iteration of the outer loop, `rows` is a set containing all unique `r` values encountered, `cols` is a set containing all unique `c` values encountered, `free_rows` is `n - len(rows)`, `free_cols` is `n - len(cols)`, `m` is the minimum of `free_rows` and `free_cols`, `result` is the final value of the last appended result in `results`.
    for res in results:
        print(res)
        
    #State of the program after the  for loop has been executed: `results` is a non-empty list containing all the elements originally stored in `results`, `res` is the last element in the list `results`, and all elements in `results` are printed.
#Overall this is what the function does:The function processes a series of test cases where each test case consists of integers \( t \), \( n \), \( k \), \( r_i \), and \( c_i \). For each test case, it calculates and stores the product of the first \( m \) natural numbers (where \( m \) is the minimum between the number of unique row indices and the number of unique column indices) modulo \( MOD \). After processing all test cases, it prints the results for each test case. If no unique row or column indices are provided, the function still processes the test case correctly by considering the full range of possible indices. Edge cases such as when all rows or columns are identical, leading to zero unique indices, are handled appropriately by ensuring the product calculation considers the remaining indices.

