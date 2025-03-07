#State of the program right berfore the function call: row is a list of non-negative integers where the first and last elements are 0, representing the depths of the river cells in a single row. d is a positive integer such that 1 <= d <= len(row) - 1, representing the maximum distance between adjacent supports.
def func_1(row, d):
    for i in range(0, d - 1):
        row[i] = row[i] + 1
        
    #State: The first `d-1` elements of the `row` list are incremented by 1, while the rest of the elements in the `row` list remain unchanged. The value of `d` remains the same.
    for i in range(d - 1, len(row)):
        row[i] = (min(row[max(0, i - (d + 1)):i]) if i > 0 else 0) + row[i] + 1
        
    #State: The first `d-1` elements of the `row` list are incremented by 1, and each element from `row[d-1]` to `row[len(row)-1]` is updated to be the minimum value of the previous `d` elements (including the incremented first `d-1` elements) plus the current value plus 1. The value of `d` remains unchanged.
    return row[-1]
    #The program returns the last element of the `row` list, which has been updated to be the minimum value of the previous `d` elements (including the first `d-1` elements that were incremented by 1) plus the current value plus 1.
#Overall this is what the function does:The function `func_1` accepts a list `row` of non-negative integers where the first and last elements are 0, and a positive integer `d` such that 1 <= d <= len(row) - 1. It increments the first `d-1` elements of `row` by 1. Then, for each element from `row[d-1]` to `row[len(row)-1]`, it updates the element to be the minimum value of the previous `d` elements (including the incremented first `d-1` elements) plus the current value plus 1. Finally, the function returns the last element of the updated `row` list.

#State of the program right berfore the function call: The function `func_2` does not take any parameters directly, but it reads input from the standard input. The first line of input contains four integers n, m, k, and d such that 1 ≤ k ≤ n ≤ 100, 3 ≤ m ≤ 2 * 10^5, and 1 ≤ d ≤ m. The next n lines each contain m integers representing the depths of the river cells, where a_{i,1} = a_{i,m} = 0 for all 1 ≤ i ≤ n.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: Output State: `n`, `m`, `k`, and `d` are unchanged; `rows` is unchanged; `costs` is unchanged; `total_costs` is a list of length `n - (k - 1)`, where each element is the sum of `k` consecutive elements from the `costs` list starting from index `i`.
    print(min(total_costs))
    #This is printed: min(total_costs) (where total_costs is a list of sums of k consecutive elements from the costs list)
#Overall this is what the function does:The function `func_2` reads input from the standard input, including four integers `n`, `m`, `k`, and `d`, and a grid of `n` rows and `m` columns representing river depths. It computes the minimum cost of a sequence of `k` consecutive rows, where the cost of each row is determined by a helper function `func_1`. The final state of the program after the function concludes is that `n`, `m`, `k`, and `d` remain unchanged, the grid `rows` is unchanged, the list `costs` contains the computed costs for each row, and the list `total_costs` contains the sums of `k` consecutive elements from the `costs` list. The function prints the minimum value from `total_costs`.

