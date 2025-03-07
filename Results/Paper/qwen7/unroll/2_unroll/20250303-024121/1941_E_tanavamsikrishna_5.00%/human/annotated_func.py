#State of the program right berfore the function call: row is a list of non-negative integers representing the depths of the river cells in a row, and d is a positive integer representing the maximum allowed distance between adjacent supports.
def func_1(row, d):
    for i in range(0, d - 1):
        row[i] = row[i] + 1
        
    #State: Output State: row is a list where each element at index i (0 <= i < d-1) has its value incremented by 1 compared to the initial state, while the rest of the elements remain unchanged.
    for i in range(d - 1, len(row)):
        row[i] = (min(row[max(0, i - (d + 1)):i]) if i > 0 else 0) + row[i] + 1
        
    #State: Output State: row is a list where each element at index i (0 <= i < d-1) has its value incremented by 1 compared to the initial state, and for each element at index i (d-1 <= i < len(row)), it is set to the minimum value of the previous d+1 elements (considering the boundary conditions), plus its original value plus 1.
    return row[-1]
    #The program returns the last element of the list 'row', which is the minimum value among the last d+1 elements of the list, plus its original value plus 1.
#Overall this is what the function does:The function accepts a list of non-negative integers `row` and a positive integer `d`. It increments the first `d-1` elements of `row` by 1, then sets each subsequent element to the minimum value among the previous `d+1` elements plus its original value plus 1. Finally, it returns the last element of the modified `row`, which is the minimum value among the last `d+1` elements of the list, plus its original value plus 1.

#State of the program right berfore the function call: (n, m, k, d) are integers where 1 ≤ k ≤ n ≤ 100, 3 ≤ m ≤ 2 × 10^5, and 1 ≤ d ≤ m. rows is a list of n lists, where each inner list contains m positive integers representing the depths of the river cells, and the first and last elements of each inner list are 0. The sum of n × m for all sets of input data does not exceed 2 × 10^5.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: Output State: `total_costs` is a list of length `n - (k - 1)` where each element is the sum of `k` consecutive elements from the `costs` list. The initial `costs` list and other variables (`n`, `m`, `k`, `d`, `rows`) retain their original values, and `total_costs` is populated with these sums.
    print(min(total_costs))
    #This is printed: min(total_costs) (where total_costs is a list of length n - (k - 1) containing the sums of k consecutive elements from the costs list)
#Overall this is what the function does:The function accepts four parameters (n, m, k, d) and a list of n lists (rows). It calculates the sum of k consecutive elements from the costs list, which is derived from the input rows list using the parameter d. The function then finds the minimum value among these sums and prints it. The final state of the program includes the original values of n, m, k, d, and rows, while introducing a new list called total_costs containing the calculated sums.

