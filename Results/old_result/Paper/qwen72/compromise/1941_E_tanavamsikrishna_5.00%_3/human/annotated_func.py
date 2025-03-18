#State of the program right berfore the function call: row is a list of integers where the first and last elements are 0, and d is a positive integer such that 1 <= d <= len(row).
def func_1(row, d):
    for i in range(0, d - 1):
        row[i] = row[i] + 1
        
    #State: row is a list of integers where the first d-1 elements are incremented by 1, and the rest of the elements remain unchanged, including the last element which is still 0. The value of d remains the same.
    for i in range(d - 1, len(row)):
        row[i] = (min(row[max(0, i - (d + 1)):i]) if i > 0 else 0) + row[i] + 1
        
    #State: Output State: The first d-1 elements of the list `row` are incremented by 1, and the rest of the elements (from index d-1 to the end) are set to the minimum value of the previous d elements plus 1. The last element of the list remains 0. The value of `d` remains unchanged.
    return row[-1]
    #The program returns 0.
#Overall this is what the function does:The function `func_1` accepts a list `row` of integers where the first and last elements are 0, and a positive integer `d` such that 1 <= d <= len(row). It modifies the list `row` by incrementing the first `d-1` elements by 1 and setting the rest of the elements (from index `d-1` to the end) to the minimum value of the previous `d` elements plus 1. The last element of the list remains 0. The function always returns 0, and the value of `d` remains unchanged.

#State of the program right berfore the function call: No variables are passed to the function `func_2`. The function reads input from the standard input, where the first line contains four integers n, m, k, and d such that 1 ≤ k ≤ n ≤ 100, 3 ≤ m ≤ 2 · 10^5, and 1 ≤ d ≤ m. The following n lines each contain m integers representing the depths of the river cells, with the constraints 0 ≤ a_{i, j} ≤ 10^6 and a_{i, 1} = a_{i, m} = 0.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: `total_costs` is a list of length `n - (k - 1)`, where each element is the sum of `k` consecutive elements from the `costs` list. The values of `n`, `m`, `k`, `d`, `rows`, and `costs` remain unchanged.
    print(min(total_costs))
    #This is printed: min(total_costs) (where min(total_costs) is the minimum sum of k consecutive elements from the costs list)
#Overall this is what the function does:The function `func_2` reads input from the standard input, where the first line contains four integers `n`, `m`, `k`, and `d` with specific constraints. It then reads `n` lines, each containing `m` integers representing the depths of river cells. The function calculates the cost for each row using the `func_1` function and stores these costs in a list. It computes the sum of `k` consecutive elements from this list for each possible segment and prints the minimum of these sums. The function does not return any value. After the function concludes, the input variables `n`, `m`, `k`, `d`, `rows`, and `costs` remain unchanged, and the minimum sum of `k` consecutive costs is printed to the standard output.

