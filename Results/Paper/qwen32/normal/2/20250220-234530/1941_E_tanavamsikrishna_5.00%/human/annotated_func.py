#State of the program right berfore the function call: row is a list of integers representing the depths of the river cells in a single row, and d is a positive integer representing the maximum distance between supports.
def func_1(row, d):
    for i in range(0, d - 1):
        row[i] = row[i] + 1
        
    #State: Elements at indices 0 to d-2 in `row` are each incremented by d-1, and elements at indices d-1 and beyond remain unchanged.
    for i in range(d - 1, len(row)):
        row[i] = (min(row[max(0, i - (d + 1)):i]) if i > 0 else 0) + row[i] + 1
        
    #State: Elements at indices 0 to d-2 are incremented by d-1. For each index i from d-1 to the end of the list, row[i] is updated to min(row[max(0, i-(d+1)):i]) + row[i] + 1.
    return row[-1]
    #The program returns the value at the last index of the list `row` after the specified operations have been performed.
#Overall this is what the function does:The function modifies a list of integers (`row`) by incrementing certain elements based on a specified distance (`d`). It then returns the value of the last element in the modified list.

#State of the program right berfore the function call: n is a positive integer representing the number of rows, m is a positive integer representing the number of columns, k is a positive integer representing the number of bridges, and d is a positive integer representing the maximum distance between supports such that 1 <= k <= n and 3 <= m and 1 <= d <= m.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: `n` is a positive integer representing the number of rows, `m` is a positive integer representing the number of columns, `k` is a positive integer representing the number of bridges, `d` is a positive integer representing the maximum distance between supports such that 1 <= k <= n and 3 <= m and 1 <= d <= m, `rows` is a 2D list of integers with dimensions `n` x `m`, `costs` is a list of length `n` where each element is the result of `func_1` applied to the corresponding row in `rows`, `total_costs` is a list containing the sum of `costs[i:i + k]` for all `i` from `0` to `n - k`.
    print(min(total_costs))
    #This is printed: min(total_costs) (where total_costs is a list of sums of k consecutive elements in costs, and costs is a list of values obtained by applying func_1 to each row in rows)
#Overall this is what the function does:The function reads input values for the number of rows (`n`), columns (`m`), bridges (`k`), and maximum distance between supports (`d`). It processes a 2D list of integers representing rows and calculates a cost for each row using `func_1`. Then, it computes the sum of costs for every possible set of `k` consecutive rows and prints the minimum of these sums.

